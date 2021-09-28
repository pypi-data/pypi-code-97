import numpy as np

import trisicell as tsc


def remove_mut_by_list(adata, alist):
    """Remove a list of mutations from the data.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    alist : :obj:`list`
        A list of mutations.
    """

    adata._inplace_subset_var(np.setdiff1d(adata.var_names, alist))
    tsc.logg.info(f"Matrix with n_obs × n_vars = {adata.shape[0]} × {adata.shape[1]}")


def keep_mut_by_list(adata, alist):
    """Keep a list of mutations from the data.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    alist : :obj:`list`
        A list of mutations.
    """

    adata._inplace_subset_var(np.intersect1d(alist, adata.var_names))
    tsc.logg.info(f"Matrix with n_obs × n_vars = {adata.shape[0]} × {adata.shape[1]}")


def remove_cell_by_list(adata, alist):
    """Remove a list of cells from the data.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    alist : :obj:`list`
        A list of cells.
    """

    adata._inplace_subset_obs(np.setdiff1d(adata.obs_names, alist))
    tsc.logg.info(f"Matrix with n_obs × n_vars = {adata.shape[0]} × {adata.shape[1]}")


def keep_cell_by_list(adata, alist):
    """Keep a list of cells from the data.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    alist : :obj:`list`
        A list of mutations.
    """

    adata._inplace_subset_obs(np.intersect1d(alist, adata.obs_names))
    tsc.logg.info(f"Matrix with n_obs × n_vars = {adata.shape[0]} × {adata.shape[1]}")


def filter_mut_vaf_greater_than_coverage_mutant_greater_than(
    adata, min_vaf=0.2, min_coverage_mutant=20, min_cells=1
):
    """Remove mutations based on the VAF and coverage.

    This function removes mutations that don't have coverage
    greater than `min_coverage_mutant` and VAF greater than
    `min_vaf` for at least `min_cells`

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    min_vaf : :obj:`float`, optional
        Minimum VAF, by default 0.2
    min_coverage_mutant : :obj:`int`, optional
        Minimum VAF, by default 20
    min_cells : :obj:`int`, optional
        Minimum VAF, by default 1
    """

    V = adata.to_df(layer="mutant")
    T = adata.to_df(layer="total")
    df = V / T
    good_muts = ((df >= min_vaf) & (V >= min_coverage_mutant)).sum(axis=0) >= min_cells
    keep_mut_by_list(adata, adata.var_names.to_numpy()[good_muts])


def filter_mut_mutant_must_present_in_at_least(adata, min_cells=2):
    """Remove mutations based on the mutant status.

    This function removes mutations that don't have the status of mutant
    in at least `min_cells` cells.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    min_cells : :obj:`int`, optional
        Minimum number of cells, by default 1
    """

    G = adata.layers["genotype"]
    good_muts = ((G == 1) | (G == 3)).sum(axis=0) >= min_cells
    keep_mut_by_list(adata, adata.var_names.to_numpy()[good_muts])


def filter_mut_reference_must_present_in_at_least(adata, min_cells=1):
    """Remove mutations based on the wild-type status.

    This function removes mutations that don't have the status of wild-type
    in at least `min_cells` cells. Note that mutations that are present in all cells
    will not be filtered out by this function.

    Parameters
    ----------
    adata : :class:`anndata.AnnData`
        The input readcount data.
    min_cells : :obj:`int`, optional
        Minimum number of cells, by default 1
    """

    G = adata.layers["genotype"]
    good_muts = ((G == 0).sum(axis=0) >= min_cells) | (
        ((G == 1) | (G == 3)).sum(axis=0) == adata.shape[0]
    )
    keep_mut_by_list(adata, adata.var_names.to_numpy()[good_muts])


def build_scmatrix(adata):
    G = adata.layers["genotype"]
    adata.X[G == 0] = 0
    adata.X[(G == 1) | (G == 3)] = 1
    adata.X[G == 2] = 3
    adata.X = adata.X.astype("int")

    # M = adata.layers["mutant"]
    # T = adata.layers["total"]
    # adata.X[T != -1] = 3
    # adata.X[T > 0] = 0
    # adata.X[M > 0] = 1
    # adata.X = adata.X.astype("int")


def statistics(adata):
    G = adata.layers["genotype"]
    t = adata.shape[0] * adata.shape[1]
    a = (G == 0).sum().sum()
    b = (G == 1).sum().sum()
    c = (G == 2).sum().sum()
    d = (G == 3).sum().sum()
    tsc.logg.info(f"size = {adata.shape[0]} × {adata.shape[1]}")
    tsc.logg.info(f"    HOM_REF = {a:6d} ({100*a/t:2.1f}%)")
    tsc.logg.info(f"    HET     = {b:6d} ({100*b/t:2.1f}%)")
    tsc.logg.info(f"    HOM_ALT = {d:6d} ({100*d/t:2.1f}%)")
    tsc.logg.info(f"    UNKNOWN = {c:6d} ({100*c/t:2.1f}%)")


def filter_snpeff(adata, exome=False):
    bad = [
        "Annotation_Impact",
        "Gene_ID",
        "Feature_ID",
        "Rank",
        "cDNA.pos / cDNA.length",
        "CDS.pos / CDS.length",
        "AA.pos / AA.length",
        "Distance",
        "ERRORS / WARNINGS / INFO",
    ]
    adata.var.drop(bad, axis=1, inplace=True)
    a = adata.var.Transcript_BioType == "protein_coding"
    b = adata.var.Feature_Type == "transcript"
    c = adata.var.Annotation.isin(["synonymous_variant", "missense_variant"])
    d = adata.var.ALT.apply(lambda x: False if "," in x else True)
    adata._inplace_subset_var(a & b & c & d)
    adata.var.drop(["Feature_Type", "Transcript_BioType"], axis=1, inplace=True)
    if exome:
        # tumor_obs = np.setdiff1d(adata.obs_names, ["NB"])[0]
        tumor_obs = adata.obs_names[adata.obs_names.str.contains("_Tumor")][0]
        adata._inplace_subset_obs(adata.obs_names.str.contains(tumor_obs))
        adata.var["Mutant"] = adata.layers["mutant"][0]
        adata.var["Total"] = adata.layers["total"][0]
        adata.var["VAF"] = adata.var["Mutant"] / adata.var["Total"]
        adata.var["SAMPLE"] = tumor_obs
