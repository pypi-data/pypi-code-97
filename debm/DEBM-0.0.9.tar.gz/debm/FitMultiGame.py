import numpy as np
from tqdm import tqdm
class FitMultiGame(): #All models should be of the same type
    def __init__(self,models,obs_choices):
        if len(models)!=len(obs_choices):
            raise Exception("Number of models and observed choices array differ")
        self._models=models
        self._obs_choices=obs_choices
    def CalcLoss(self,par,loss,scope):
        losses=np.zeros(len(self._models))
        for i,m in enumerate(self._models):
            m.set_obs_choices(self._obs_choices[i])
            l=m.CalcLoss(par,loss,scope)
            losses[i]=l
        if loss.upper()=="MSE":
            return(np.mean(losses))
        elif loss.upper()=="LL":
            return(np.sum(losses))        
    def OptimizeBF(self,pars_dicts,pb=False,*args): #Brute force - try all in list
        """
        pars_dicts should be a list of dicts. e.g., [{'alpha':2},{'alpha':4}]
        """
        minloss=9999
        bestp=None
        tmpm_array=[]
        for p in tqdm(pars_dicts,disable=not pb):
            tmpm=self.CalcLoss(p,*args)
            tmpm_array.append(tmpm)
            if tmpm<minloss:
                minloss=tmpm
                bestp=p
        res=dict(bestp=bestp,minloss=minloss,losses=tmpm_array,parameters_checked=pars_dicts)                
        return res