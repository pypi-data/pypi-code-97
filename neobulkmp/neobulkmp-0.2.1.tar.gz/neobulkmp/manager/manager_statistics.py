import os
import psutil
import graphio
import humanfriendly
from collections import OrderedDict
import time
import graphio
from typing import TYPE_CHECKING, Type, Union, Dict
from ..worker_base import Progress

if TYPE_CHECKING:
    from .manager import Manager


class Statistics:
    NodeSets_done_timeline: OrderedDict = None
    RelSets_done_timeline: OrderedDict = None
    graph_objects_loaded_counts: OrderedDict = None
    graph_objects_cached_counts: OrderedDict = None
    management_ticks_timeline: OrderedDict = None

    def __init__(self, manager):
        self.manager: "Manager" = manager
        self.last_tick_sourcing_workers_done = []
        self.start_time = time.time()

        self.NodeSets_done_timeline = OrderedDict()
        self.RelSets_done_timeline = OrderedDict()
        self.graph_objects_loaded_counts = OrderedDict()
        self.graph_objects_cached_counts = OrderedDict()
        self.management_ticks_timeline = OrderedDict()

    def update_statistics(
        self, finished_sourcing_workers: list, finished_loading_workers: list
    ):
        current_time = time.time()
        # Save NodeSets/RelSets Workers timeline
        self.NodeSets_done_timeline[current_time] = [
            w for w in finished_loading_workers if w.set_meta.type == graphio.NodeSet
        ]

        self.RelSets_done_timeline[current_time] = [
            w
            for w in finished_loading_workers
            if w.set_meta.type == graphio.RelationshipSet
        ]

        # Save Labels/Rels amount loaded
        self.graph_objects_loaded_counts[
            current_time
        ] = self.manager.cache.get_report_graphsets_loaded()

        # Save Labels/Rels amount loaded
        self.graph_objects_cached_counts[
            current_time
        ] = self.manager.cache.get_report_graphsets_cached()

        # Save amount of management ticks
        self.management_ticks_timeline[current_time] = self.manager.management_ticks

    def get_management_ticks_per_n_sec(
        self, n: int = 1, timeframe: int = 20, object_type=None
    ) -> int:
        current_time = time.time()
        running_time = current_time - self.start_time
        if running_time < timeframe:
            timeframe_start = self.start_time
        else:
            timeframe_start = current_time - timeframe

        relevant_data = OrderedDict()
        for timestamp, tick_count in self.management_ticks_timeline.items():
            if timestamp > timeframe_start:
                relevant_data[timestamp] = tick_count
        relevnt_tick_counts = list(relevant_data.values())
        if len(relevnt_tick_counts) < 2:
            tick_count = 0
        else:
            tick_count = (
                relevnt_tick_counts[len(relevant_data) - 1] - relevnt_tick_counts[0]
            )
        return (tick_count / (current_time - timeframe_start)) * n

    def get_graphobjects_count_loaded_per_n_sec(
        self, n: int = 1, timeframe: int = 20, object_type: str = None
    ) -> int:
        """[summary]

        Args:
            n (int, optional): Timeresolution in sec. Defaults to 1.
            timeframe (int, optional): Take last n seconds into account to calculate median value. Defaults to 20.
            object_type (str, optional): "Nodes" to only count Nodes per second, "Relations" to only count rels per second or None to count both. Defaults to None.

        Returns:
            int: Integer as objects per n seconds loaded
        """
        return self._get_graphobjects_count_per_n_sec(
            n=n, timeframe=timeframe, object_type=object_type, target="Loaded"
        )

    def get_graphobjects_count_cached_per_n_sec(
        self, n: int = 1, timeframe: int = 20, object_type: str = None
    ) -> int:
        """[summary]

        Args:
            n (int, optional): Timeresolution in sec. Defaults to 1.
            timeframe (int, optional): Take last n seconds into account to calculate median value. Defaults to 20.
            object_type (str, optional): "Nodes" to only count Nodes per second, "Relations" to only count rels per second or None to count both. Defaults to None.

        Returns:
            int: Integer as objects per n seconds loaded
        """
        return self._get_graphobjects_count_per_n_sec(
            n=n, timeframe=timeframe, object_type=object_type, target="Cached"
        )

    def _get_graphobjects_count_per_n_sec(
        self,
        n: int = 1,
        timeframe: int = 20,
        object_type: str = None,
        target: str = "Loaded",
    ) -> int:
        """[summary]

        Args:
            n (int, optional): Timeresolution in sec. Defaults to 1.
            timeframe (int, optional): Take last n seconds into account to calculate median value. Defaults to 20.
            object_type (str, optional): "Nodes" to only count Nodes per second, "Relations" to only count rels per second or None to count both. Defaults to None.
            target (str, optional): Do you want to count graphsets loaded into the neo4j DB use "Loaded" or do you want to count cached graphobjects into the cache backend (e.g. redis) use "Cached". Defaults to "Loaded"
        Returns:
            int: Integer as objects per n seconds loaded
        """
        current_time = time.time()
        running_time = current_time - self.start_time
        if running_time < timeframe:
            timeframe_start = self.start_time
        else:
            timeframe_start = current_time - timeframe
        relevant_data = OrderedDict()

        for timestamp, data in (
            self.graph_objects_loaded_counts.items()
            if target == "Loaded"
            else self.graph_objects_cached_counts.items()
        ):
            if timestamp > timeframe_start:
                relevant_data[timestamp] = data
        count_before_and_after = [0, 0]
        if len(relevant_data) == 0:
            return 0
        for index, data_position in enumerate([0, len(relevant_data) - 1]):
            count_all = 0
            report = list(relevant_data.values())[data_position]
            if object_type in [None, "Nodes"]:
                for graphobject_name, count in report["Nodes"].items():
                    count_all += count
            if object_type in [None, "Relations"]:
                for graphobject_name, count in report["Relations"].items():
                    count_all += count
            count_before_and_after[index] = count_all
        if len(relevant_data) < 2:
            count_before_and_after[0] = 0
        return ((count_before_and_after[1] - count_before_and_after[0]) / timeframe) * n

    def get_count_graphsets_loaded_per_n_sec(
        self,
        n: int = 1,
        timeframe: int = 20,
        graphset_type: Type[Union[graphio.NodeSet, graphio.RelationshipSet]] = None,
    ):
        current_time = time.time()
        running_time = current_time - self.start_time
        if running_time < timeframe:
            timeframe_start = self.start_time
        else:
            timeframe_start = current_time - timeframe

        workers = []
        for timestamp, workers_in_slot in self.NodeSets_done_timeline.items():
            if timestamp > timeframe_start:
                if graphset_type is None or graphset_type == graphio.NodeSet:
                    workers.extend(workers_in_slot)
                if graphset_type is None or graphset_type == graphio.RelationshipSet:
                    # this is a little bit hacky but we know for sure that the keys in self.RelSets_done_timeline and self.NodeSets_done_timeline are always in sync
                    workers.extend(self.RelSets_done_timeline[timestamp])
        return (len(workers) / (current_time - timeframe_start)) * n

    def get_count_running_sourcing_workers(self) -> int:
        return len(
            self.manager.manager_sourcing._get_workers(status=("initial", "running"))
        )

    def get_count_left_sourcing_workers(self) -> int:
        return len(self.manager.manager_sourcing.workers) - len(
            self.manager.manager_sourcing._get_workers(progress="complete")
        )

    def get_memory_consumed_by_loaders(self):
        mem_total_bytes = 0
        for worker in self.manager.manager_loading._get_workers(status="running"):
            process = psutil.Process(worker.pid)
            mem_total_bytes += process.memory_info()[0]
        return mem_total_bytes

    def get_memory_consumed_by_sourcing_workers(self):
        mem_total_bytes = 0
        for worker in self.manager.manager_sourcing._get_workers(status="running"):
            process = psutil.Process(worker.pid)
            mem_total_bytes += process.memory_info()[0]
        return mem_total_bytes

    def get_memory_consumed_by_manager(self):
        process = psutil.Process(os.getpid())
        return process.memory_info()[0]

    def is_sourcing_phase_done(self):
        return self.manager.manager_sourcing.is_done()

    def get_memory_available(self):
        return getattr(psutil.virtual_memory(), "available")

    def get_memory_total(self):
        return getattr(psutil.virtual_memory(), "total")

    def get_memory_used(self):
        return getattr(psutil.virtual_memory(), "used")

    def get_cache_storage_total(self) -> int:
        return self.manager.strategy.cache_storage_total

    def get_cache_storage_available(self) -> int:
        return self.get_cache_storage_total() - self.get_cache_storage_used()

    def get_cache_storage_used(self) -> int:
        return self.manager.cache.storage_used()

    def get_cached_graphobjects_total(self, object_type: str = None) -> int:
        if not self.graph_objects_cached_counts:
            return 0
        last_count_stats = self.graph_objects_cached_counts[
            next(reversed(self.graph_objects_cached_counts))
        ]
        total_count = 0
        if object_type in [None, "Relations"]:
            for label, count in last_count_stats["Relations"].items():
                total_count += count
        if object_type in [None, "Nodes"]:
            for label, count in last_count_stats["Nodes"].items():
                total_count += count
        return total_count

    def get_loaded_graphobjects_total(self, object_type: str = None) -> int:
        if not self.graph_objects_loaded_counts:
            return 0
        last_count_stats = self.graph_objects_loaded_counts[
            next(reversed(self.graph_objects_loaded_counts))
        ]
        total_count = 0
        if object_type in [None, "Relations"]:
            for label, count in last_count_stats["Relations"].items():
                total_count += count
        if object_type in [None, "Nodes"]:
            for label, count in last_count_stats["Nodes"].items():
                total_count += count
        return total_count

    def get_cached_graphobjects_current(self) -> int:
        pass

    def get_cache_storage_level(self) -> str:
        mem_full_perc = (
            self.get_cache_storage_used() * 100
        ) / self.get_cache_storage_total()
        if self.manager.strategy.cache_storage_clogged_limit <= mem_full_perc:
            return "RED"
        elif self.manager.strategy.cache_storage_warning_limit <= mem_full_perc:
            return "ORANGE"
        else:
            return "GREEN"

    def get_cache_storage_used_by_relSets(self):
        size = 0
        for rel_meta in self.manager.cache.list_SetsMeta(
            set_type=graphio.RelationshipSet
        ):
            size += rel_meta.total_size_bytes
        return size

    def get_cache_storage_used_by_nodeSets(self):
        size = 0
        for rel_meta in self.manager.cache.list_SetsMeta(set_type=graphio.NodeSet):
            size += rel_meta.total_size_bytes
        return size

    def get_report(self):
        report = {}

        report["General"] = {}

        gen_rep = report["General"]

        gen_rep["running_time_sec"] = {
            "val": time.time() - self.start_time,
            "desc": "Running time",
            "humanfriendly_transformer": humanfriendly.format_timespan,
        }

        gen_rep["management_tick_per_sec"] = {
            "val": self.get_management_ticks_per_n_sec(),
            "desc": "Management ticks per second",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        report["Sourcing"] = {}

        src_rep = report["Sourcing"]

        src_rep["cores_avail_no"] = {
            "val": self.manager.strategy.amount_sourcing_cores(),
            "desc": "Sourcing Workers amount of cores allocated",
        }
        src_rep["workers_total_no"] = {
            "val": self.manager.manager_sourcing.worker_count_total,
            "desc": "Sourcing Workers amount total",
        }

        src_rep["workers_fin_no"] = {
            "val": len(self.manager.manager_sourcing.finished_workers),
            "desc": "Sourcing Workers amount finished",
        }

        src_rep["workers_running_no"] = {
            "val": len(self.manager.manager_sourcing._get_workers(status="running")),
            "desc": "Sourcing Workers amount running",
        }

        report["Cache"] = {}

        cache_rep = report["Cache"]

        cache_rep["relSet_no"] = {
            "val": len(self.manager.cache.list_SetsMeta(graphio.RelationshipSet)),
            "desc": "RelationSets count in cache",
        }
        cache_rep["relSet_size"] = {
            "val": self.get_cache_storage_used_by_relSets(),
            "desc": "RelationSets size in cache",
            "humanfriendly_transformer": humanfriendly.format_size,
        }

        cache_rep["rels_per_sec"] = {
            "val": self.get_graphobjects_count_cached_per_n_sec(
                object_type="Relations"
            ),
            "desc": "Relations cached per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        cache_rep["nodeSet_no"] = {
            "val": len(self.manager.cache.list_SetsMeta(graphio.NodeSet)),
            "desc": "NodeSets count in cache",
        }
        cache_rep["nodeSet_size"] = {
            "val": self.get_cache_storage_used_by_nodeSets(),
            "desc": "NodeSets size in cache",
            "humanfriendly_transformer": humanfriendly.format_size,
        }

        cache_rep["nodes_per_sec"] = {
            "val": self.get_graphobjects_count_cached_per_n_sec(object_type="Nodes"),
            "desc": "Nodes cached per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }
        #

        cache_rep["cache_storage_status"] = {
            "val": self.get_cache_storage_level(),
            "desc": "Cache storage health status",
        }

        cache_storage_level_details = f"{int(100 - ((self.get_cache_storage_used() * 100) / self.get_cache_storage_total()))}% Free ({humanfriendly.format_size(self.get_cache_storage_used())} used of {humanfriendly.format_size(self.get_cache_storage_total())})"

        cache_rep["cache_storage_status_details"] = {
            "val": cache_storage_level_details,
            "desc": "Cache storage status details",
        }

        report["Loading"] = {}

        load_rep = report["Loading"]

        load_rep["cores_avail_no"] = {
            "val": self.manager.strategy.amount_loading_cores(),
            "desc": "Loading Workers amount of cores allocated",
        }
        load_rep["workers_running_no"] = {
            "val": len(self.manager.manager_loading._get_workers(status="running")),
            "desc": "Loading Workers amount running",
        }
        load_rep["workers_fin_no"] = {
            "val": len(self.manager.manager_loading.finished_workers),
            "desc": "Loading Workers amount finished",
        }

        load_rep["workers_relsets_run_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    status=("running"),
                    tag=self.manager.manager_loading.worker_tag_relsets,
                )
            ),
            "desc": "Loading RelSets Workers amount running",
        }

        load_rep["workers_relsets_fin_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    progress=Progress.COMPLETE,
                    tag=self.manager.manager_loading.worker_tag_relsets,
                )
            ),
            "desc": "Loading RelSets Workers amount finished",
        }

        load_rep["workers_relsets_wait_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    progress=Progress.DRAIN_ORDERED,
                    tag=self.manager.manager_loading.worker_tag_relsets,
                )
            ),
            "desc": "RelSets Workers waiting for NodeSet drain",
        }

        load_rep["labels_blocked_for_rels"] = {
            "val": len(self.manager._get_blocked_labels()),
            "desc": "Amount of labels blocked for relation loading",
        }

        load_rep["relSet_per_sec"] = {
            "val": self.get_count_graphsets_loaded_per_n_sec(
                graphset_type=graphio.RelationshipSet
            ),
            "desc": "RelationSets loaded per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        load_rep["rels_per_sec"] = {
            "val": self.get_graphobjects_count_loaded_per_n_sec(
                object_type="Relations"
            ),
            "desc": "Relations loaded per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        load_rep["workers_relsets_run_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    status=("running"),
                    tag=self.manager.manager_loading.worker_tag_relsets,
                )
            ),
            "desc": "Loading RelSets Workers amount running",
        }

        load_rep["workers_NodeSets_run_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    progress=(Progress.QUEUED, Progress.LOADING),
                    tag=self.manager.manager_loading.worker_tag_nodesets,
                )
            ),
            "desc": "Loading NodeSets Workers running or queded",
        }

        load_rep["workers_NodeSets_fin_no"] = {
            "val": len(
                self.manager.manager_loading._get_workers(
                    progress=Progress.COMPLETE,
                    tag=self.manager.manager_loading.worker_tag_nodesets,
                )
            ),
            "desc": "Loading NodeSets Workers amount finished",
        }

        load_rep["nodeSet_per_sec"] = {
            "val": self.get_count_graphsets_loaded_per_n_sec(
                graphset_type=graphio.NodeSet
            ),
            "desc": "NodeSets loaded per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        load_rep["nodes_per_sec"] = {
            "val": self.get_graphobjects_count_loaded_per_n_sec(object_type="Nodes"),
            "desc": "Nodes loaded per sec",
            "humanfriendly_transformer": "{:.2f}/s".format,
        }

        report["SyncControl"] = {}
        sync_rep = report["SyncControl"]

        sync_rep["sourcing_paused"] = {
            "val": str(not self.manager.cache.store_is_available()),
            "desc": "Sourcing is paused to let loading catch up",
        }
        sync_rep["cached_total"] = {
            "val": self.get_cached_graphobjects_total(),
            "desc": "Count of Graphobjects inserted into cache",
            "humanfriendly_transformer": humanfriendly.format_number,
        }

        sync_rep["loaded_total"] = {
            "val": self.get_loaded_graphobjects_total(),
            "desc": "Count of Graphobjects loaded into Neo4j",
            "humanfriendly_transformer": humanfriendly.format_number,
        }

        sync_rep["cache_to_load_advantage_count"] = {
            "val": sync_rep["cached_total"]["val"] - sync_rep["loaded_total"]["val"],
            "desc": "Advantage of cached to loaded graphobjects in graphobject",
            "humanfriendly_transformer": humanfriendly.format_number,
        }

        sync_rep["cache_to_load_advantage_count_max"] = {
            "val": self.manager.strategy.max_advantage_cache_graphobjects_count,
            "desc": "Max advantage count before pausing sourcing workers",
            "humanfriendly_transformer": humanfriendly.format_number,
        }
        sync_rep["cache_to_load_advantage"] = {
            "val": (
                (
                    (sync_rep["cached_total"]["val"] / sync_rep["loaded_total"]["val"])
                    * 100
                )
                - 100
            )
            if sync_rep["loaded_total"]["val"] not in [None, 0]
            else 0,
            "desc": "Percental advantage of cached to loaded graphobjects",
            "humanfriendly_transformer": "{:.2f} %".format,
        }

        report["Memory"] = {}
        mem_rep = report["Memory"]

        mem_rep = report["Memory"]

        memory_status = f"{humanfriendly.format_size(self.get_memory_available())} available - {humanfriendly.format_size(self.get_memory_used())} used of {humanfriendly.format_size(self.get_memory_total())}"

        mem_rep["memory_status_details"] = {
            "val": memory_status,
            "desc": "Memory status for Manager and Workers processes",
        }

        mem_rep["memory_used_by_manager"] = {
            "val": self.get_memory_consumed_by_manager(),
            "desc": "Memory used by the manager process",
            "humanfriendly_transformer": humanfriendly.format_size,
        }

        mem_rep["memory_used_by_sourcing_workers"] = {
            "val": self.get_memory_consumed_by_sourcing_workers(),
            "desc": "Memory used by the sourcing processes",
            "humanfriendly_transformer": humanfriendly.format_size,
        }

        mem_rep["memory_used_by_loading_workers"] = {
            "val": self.get_memory_consumed_by_loaders(),
            "desc": "Memory used by the loading processes",
            "humanfriendly_transformer": humanfriendly.format_size,
        }

        return report

    def get_human_readable_report(self):

        report = self.get_report()

        report_str = "\n"
        for title, chapters in report.items():
            report_str += f"## {title}\n"
            longest_chapter_desc = max(
                [len(chapter["desc"]) for chapter in chapters.values()]
            )
            for key, chapter in chapters.items():
                if "humanfriendly_transformer" in chapter:
                    val = chapter["humanfriendly_transformer"](chapter["val"])
                else:
                    val = chapter["val"]
                row = "\t{:" + str(longest_chapter_desc) + "}: {}\n"
                report_str += row.format(chapter["desc"], val)

        return report_str
