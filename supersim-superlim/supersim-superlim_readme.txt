NOTE: This readme.txt describes a pre-release, it will be updated and
complementet with more detailed documentation in the future.


                               SuperSim
                      (repackaged för Superlim)


INTRODUCTION

This archive contains the gold standard data provided in

  Data for "SuperSim: a test set for word similarity and relatedness
  in Swedish", v1; Simon Hengchen, Nina Tahmasebi; University of
  Gothenburg; DOI 10.5281/zenodo.4660084; CC BY 4.0 to
  Hengchen/Tahmasebi

repackaged to be part of the Superlim collection

  https://spraakbanken.gu.se/resurser/superlim.

The data provided here is exactly the same, and in the same format, as
the data given in the original archive.

The original archive at Zenodo is a companion to the paper

  Hengchen, Simon and Nina Tahmasebi (2021) SuperSim: a test set for
  word similarity and relatedness in Swedish. Proceedings of NoDaLiDa
  2021, Reykjavik.

and contains benchmark code, models, and more information about the
data. Please refer to the original archive and the paper for more
details.

When you use this data, please cite the NoDaLiDa paper given above.

For questions about the present archive, or about the Superlim
project, please contact Språkbanken Text <sb-info@svenska.gu.se>.


DATA FILES

The gold standard data is given in two files in the data subdirectory
in this archive:

data/gold_relatedness.tsv:
  a tab separated values file with header, containing word relatedness
  scores for pairs of words, both per annotator and on average (final
  column).

data/gold_similarity.tsv:
  a tab separated values file with header, containing word similarity
  scores for pairs of words, both per annotator and on average (final
  column).

We refer to the paper for a discussion of the difference between word
relatedness and word similarity.


TASK

In the context of Superlim, we suggest -- as a minimum -- that
experimenters follow the methodology of Hengchen/Tahmasebi (2021), and
use their models to predict similarity or relatedness scores and
report Spearman's rho for rank correlation with similarity or
relatedness score (from the column of averages).

