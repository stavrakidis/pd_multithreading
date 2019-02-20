==================
pd_multiprocessing
==================

pd_multiprocessing provides a simple, parallelized function to apply a user defined function rowwise on a Pandas Dataframe.


Usage
=====

A typical usage looks like this

    from pd_multiprocessing.map import df_map


    def twotimes(row):
        row['col2'] = row['col1']*2
        return row


    if __name__ == '__main__':
        df = pd.DataFrame.from_dict({'col1': range(100)})
        print(df_map(twotimes, df))
