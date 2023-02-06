from bioinfokit import analys, visuz

import pandas as pd

df = pd.read_csv (r'GWAS.csv')
print (df)

visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=("#a7414a", "#696464", "#00743f", "#563838", "#6a8a82", "#a37c27", "#5edfff", "#282726", "#c0334d", "#c9753d"), gwas_sign_line=True, gwasp=5E-06, markernames=True, markeridcol='SNP', show=True)


# Add annotation to SNPs (box text),
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, gwas_sign_line=True, gwasp=5E-06,
#     markernames=True, markeridcol='SNP', gstyle=2)

# add name to specified  SNPs only
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, gwas_sign_line=True, gwasp=5E-06,
    # markernames=("rs19990", "rs40"), markeridcol='SNP')

# add name to specified  SNPs only (box text)
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, gwas_sign_line=True, gwasp=5E-06,
#     markernames=("rs19990", "rs40"), markeridcol='SNP', gstyle=2)

# change font size of SNP annotation
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, gwas_sign_line=True, gwasp=5E-06, markernames=True,
#     markeridcol='SNP', gfont=5)
# gfont is incompatible with gstyle

# add gene names to SNPs
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color,
# gwas_sign_line=True, gwasp=5E-06, markernames=({"rs19990":"gene1", "rs40":"gene2"}), markeridcol='SNP')

# change figure size
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, dim=(8,6) )

# change point size
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, dotsize=2 )

# change point transparency
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, valpha=0.2 )

# change X-axis tick label rotation
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, ar=60 )

# change figure resolution
# visuz.marker.mhat(df=df, chr='chr',pv='pvalue', color=color, r=600 )
