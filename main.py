from repetitive_procedure import RepetitiveProcedure as Algorithm

from Obj_Functions.Series_Obj_Function import obj_function as fitness,\
    subsystems as dimensions, redundancy as red_upper_bound

import pandas as pd

if __name__ == '__main__':

    alg_iterations = 100  # Generations
    pop_size = 50

    independent_runs = 50

    # Monitor Time
    import time
    start_time = time.time()

    df = pd.DataFrame()

    for i in range(independent_runs):
        print(100 * (i + 1) / independent_runs, '%')
        [Quality, Redundancy_Allocation, Reliability_Allocation
         ] = Algorithm(alg_iterations, pop_size, dimensions, red_upper_bound, fitness).results()
        # can add Slack depending the problem
        temp_df = pd.DataFrame(
            {
                'Solution_Quality': Quality,
                'Redundancy_Allocation': [Redundancy_Allocation],
                'Reliability_Allocation': [Reliability_Allocation]
            }
        )

        df = pd.concat([df, temp_df])

    df['Time'] = time.time() - start_time

    "-------------------Print to console-------------------------"
    print("\n", df.iloc[df.iloc[:, 0].idxmax(axis=0), :], "\n")
    print("\n", df.describe(), "\n")
    print(df.iloc[:, 0].idxmax(axis=0))
    "----------------------Save to csv---------------------------"
    name_of_file = 'BA-FA_Series_.csv'
    df.to_csv(name_of_file, sep=',', header=True, index=False)
