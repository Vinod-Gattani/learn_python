'''
Source:
https://towardsdatascience.com/make-your-own-super-pandas-using-multiproc-1c04f41944a1


'''
import pandas as pd

def add_features(df):
    df['question_text'] = df['question_text'].apply(lambda x:str(x))
    df["lower_question_text"] = df["question_text"].apply(lambda x: x.lower())

    return df


def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

train = parallelize_dataframe(train_df, add_features)

'''
Source:
https://towardsdatascience.com/pandaral-lel-a-simple-and-efficient-tool-to-parallelize-your-pandas-operations-on-all-your-cpus-bb5ff2a409ae
'''

from pandarallel import pandarallel

# Initialization
pandarallel.initialize()
# Standard pandas apply
df.apply(func, axis=1)

# Parallel apply
df.parallel_apply(func, axis=1)