#!/usr/bin/env python
import os
import pickle
import re
from typing import List, Dict
from utils import JobSection, PklJob
from autosubmitAPIwu.job.job_common import Status
from autosubmitAPIwu.job.job_utils import SimpleJob
import job_factory as factory 


class PklOrganizer(object):
  """ Organizes content of the pkl """
  
  def __init__(self, path_pkl):
    self.current_content = [] # type : List
    self.sim_jobs = [] # type : List[JobFactory.SimJob]
    self.post_jobs = [] # type : List[JobFactory.PostJob]
    self.transfer_jobs = [] # type : List[TransferJob.SimJob]
    self.clean_jobs = [] # type : List[CleanJob.SimJob]
    self.path = path_pkl # type : str     
    self.current_content = self._process_pkl()
    self._distribute_jobs()
    self._sort_distributed_jobs()
    self.section_jobs_map = {
      JobSection.SIM : self.sim_jobs,
      JobSection.POST : self.post_jobs,
      JobSection.TRANSFER : self.transfer_jobs,
      JobSection.CLEAN : self.clean_jobs
    } # type : Dict
    self.warnings = [] # type : List
    self._validate_current()

  def get_completed_section_jobs(self, section):
    # type : (str) -> List
    if section in self.section_jobs_map:
      return [job for job in self.section_jobs_map[section] if job.status == Status.COMPLETED]
    else:
      raise KeyError("Section not supported.")

  def get_simple_jobs(self, tmp_path):
    # type : (str) -> List[SimpleJob]
    return [SimpleJob(job.name, tmp_path, job.status) for job in self.current_content]

  def _process_pkl(self):
    # type : () -> List[PklJob]
    jobs_pkl = []    
    if os.path.exists(self.path):
      with (open(self.path, "rb")) as openfile:                
        for item in pickle.load(openfile):          
          jobs_pkl.append(PklJob(*item))
    else:
      raise Exception("Pkl file not found.")        
    return jobs_pkl
  
  def _distribute_jobs(self):
    # type : () -> None    
    for pkl_job in self.current_content:  
      if JobSection.SIM == pkl_job.section:
        self.sim_jobs.append(factory.get_job_from_factory(pkl_job.section).from_pkl(pkl_job))
      elif JobSection.POST == pkl_job.section:
        self.post_jobs.append(factory.get_job_from_factory(pkl_job.section).from_pkl(pkl_job))      
      elif JobSection.TRANSFER == pkl_job.section:
        self.transfer_jobs.append(factory.get_job_from_factory(pkl_job.section).from_pkl(pkl_job))          
      elif JobSection.CLEAN == pkl_job.section:
        self.clean_jobs.append(factory.get_job_from_factory(pkl_job.section).from_pkl(pkl_job))

  def _sort_distributed_jobs(self):
    # type : () -> None
    """ SIM jobs are sorted by start_time  """
    self._sort_list_by_start_time(self.sim_jobs)
    self._sort_list_by_finish_time(self.post_jobs)
    self._sort_list_by_finish_time(self.transfer_jobs)
    self._sort_list_by_finish_time(self.clean_jobs)

  def _validate_current(self):
    # type : () -> None
    if len(self.get_completed_section_jobs(JobSection.SIM)) == 0:
      self._add_warning("We couldn't find COMPLETED SIM jobs in the experiment.")
    if len(self.get_completed_section_jobs(JobSection.POST)) == 0:
      self._add_warning("We couldn't find COMPLETED POST jobs in the experiment. ASYPD can't be calculated.")
    if len(self.get_completed_section_jobs(JobSection.TRANSFER)) == 0 and len(self.get_completed_section_jobs(JobSection.CLEAN)) == 0:
      self._add_warning("RSYPD | There are no TRANSFER nor CLEAN (COMPLETED) jobs in the experiment, RSYPD cannot be computed.")
    if len(self.get_completed_section_jobs(JobSection.TRANSFER)) == 0 and len(self.get_completed_section_jobs(JobSection.CLEAN)) > 0:
      self._add_warning("RSYPD | There are no TRANSFER (COMPLETED) jobs in the experiment. We will use (COMPLETED) CLEAN jobs to compute RSYPD.")
  
  def _add_warning(self, message):
    # type : (str) -> None
    self.warnings.append(message)

  def _sort_list_by_finish_time(self, jobs):
    # type : (List[Job]) -> None
    if len(jobs):
      jobs.sort(key = lambda x: x.finish, reverse=False)
  
  def _sort_list_by_start_time(self, jobs):
    # type : (List[Job]) -> None
    if len(jobs):
      jobs.sort(key = lambda x: x.start, reverse=False)

  def __str__(self):
    return "Path: {5} \nTotal {0}\nSIM {1}\nPOST {2}\nTRANSFER {3}\nCLEAN {4}".format(
      len(self.current_content),
      len(self.sim_jobs),
      len(self.post_jobs),
      len(self.transfer_jobs),
      len(self.clean_jobs),
      self.path
    )
  
