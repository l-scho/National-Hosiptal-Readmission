import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import scipy.stats as stats
from scipy.stats import beta
plt.style.use('ggplot')

df = pd.read_csv('../data/Hospital_Readmissions_Reduction_Program.csv', sep=';')
grouped_by_state_and_measure = df.groupby(['State', 'Measure Name']).sum()
df_test2 = grouped_by_state_and_measure.reset_index()

def bayesian_plot(condition_name, ax):

    prior_a = 1
    prior_b = 1

    coastal = ['WA', 'CA', 'OR', 'TX', 'LA', 'FL', 'GA', 'SC', 'NC', 'VA', 'MD', 'DE', 'NJ', 'NY', 'CT', 'RI', 'MA', 'NH', 'ME']

    coastal_nomeasure_df = df_test2.loc[df_test2['State'].isin(coastal), :]
    noncoastal_nomeasure_df = df_test2.loc[~df_test2['State'].isin(coastal), :]
    coastal_df = coastal_nomeasure_df.loc[df_test2['Measure Name'] == condition_name, :]
    noncoastal_df = noncoastal_nomeasure_df.loc[df_test2['Measure Name'] == condition_name, :]

    varA_c = coastal_df['Number of Readmissions'].sum() 
    varA_n = coastal_df['Number of Discharges'].sum()
    varB_c = noncoastal_df['Number of Readmissions'].sum()
    varB_n = noncoastal_df['Number of Discharges'].sum()

    varA_posteriora = prior_a + varA_c
    varB_posteriora = prior_a + varB_c
    varA_posteriorb = prior_b + (varA_n - varA_c)
    varB_posteriorb = prior_b + (varB_n - varB_c)

    x = np.linspace(0,1,10000)
    for (a,b,s,label) in [(varA_posteriora+1, varA_posteriorb+1, "lightsalmon", "Coastal Readmission Rate for HIP-KNEE"),
                          (varB_posteriora+1, varB_posteriorb+1, "indianred", "Non-Coastal Readmission Rate for HIP-KNEE")]:
        ax.plot(x,
            stats.beta(a,b).pdf(x),
            s,
            label=label)
    ax.legend(loc="upper right")
    ax.set_xlabel("p")
    ax.set_ylabel("pdf")
    ax.set_xlim(0.036, 0.044)
    ax.set_title(f"Probabilities of" "Readmission Rate for Coastal and Non-Coastal Hospitals")

