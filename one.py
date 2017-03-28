import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    load_robot_execution_failures
download_robot_execution_failures()
timeseries, y = load_robot_execution_failures()

print (timeseries, y)

from tsfresh import extract_features
extracted_features = extract_features(timeseries, column_id="id", column_sort="time")

"""You end up with a dataframe extracted_features with all more than 1200 different extracted features. 
We will now remove all NaN values and select only the relevant features next"""

from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute

impute(extracted_features)
features_filtered = select_features(extracted_features, y)

from tsfresh import extract_relevant_features

features_filtered_direct = extract_relevant_features(timeseries, y, column_id='id', column_sort='time')

print(features_filtered_direct)
print len(features_filtered_direct)