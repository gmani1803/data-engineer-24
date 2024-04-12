# write your code here
import pandas as pd

# Assuming data is already loaded into pandas DataFrames: history and status_changes

# Process history dataset
history['attribute'] = history['mutation'].str.split('-^!^!^-').str[0]
history['old_value'] = history['mutation'].str.split('-^!^!^-').str[1]
history['new_value'] = history['mutation'].str.split('-^!^!^-').str[2]
history.drop('mutation', axis=1, inplace=True)

# Filter relevant history entries
membership_history = history[history['attribute'].isin(['customer_type', 'current_status', 'membership_form_of_payment'])]

# Process status_changes dataset
status_changes['start_date'] = pd.to_datetime(status_changes['start_date'])
status_changes['end_date'] = status_changes.groupby('customer_id')['start_date'].shift(-1)
status_changes['end_reason'] = status_changes['status'].apply(lambda x: 'expire' if x == 'FREEZE' else 'cancel' if x == 'TERMINATED' else '')

# Combine history and status_changes to get membership start and end dates
membership_dates = pd.merge(membership_history, status_changes, on='customer_id', how='inner')
membership_dates = membership_dates[['customer_id', 'start_date', 'end_date', 'end_reason']]

# Convert end_date to date format
membership_dates['end_date'] = pd.to_datetime(membership_dates['end_date']).dt.date

# Sort by customer_id and start_date
membership_dates.sort_values(by=['customer_id', 'start_date'], inplace=True)

# Output the result
print(membership_dates)
