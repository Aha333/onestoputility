# Design a job

Actually, the job means a true workflow that including data input and a series of
data manipulations.

***

Let's take an example.We want to write a job that can generate the distribution of a car type, by hour.
How do you write the code.

```
def generate_output(
    df,
    time_col,
    type_col):
    """ Generates the groups by time and type of car """
    return df.groupby([time_col,type_col].groups.iteritems()

```
However, this is probably not good.
The reason is :

* It need to constantly pass in time_col, and type_col
* The function is not clean.

What we really want is a output generator.

```
class GroupGenerator(object):
    def __init__(self,
                 df,
                 time_col,
                 type_col):
        self._df = df
        self.time_col = time_col
        self.type_col = type_col

    def agg_groups(self):
        return self._df.groupby([self.time_col,self.type_col])

```

This code is way better to wrap the functions and seal the variables that are not needed.




