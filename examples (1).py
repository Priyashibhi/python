import pandas as pd
import matplotlib.pyplot as plt
file_path = "C:\\Users\\DELL\\Downloads\\telegram_messages (1).csv"
df= pd.read_csv(file_path)
df.info()
#Frequent contributors
contributor_counts = df['Sender Name'].value_counts()
most_frequent_contributors = contributor_counts.head(10)
print("Top contributors by message count:")
print(most_frequent_contributors)

# specific days with higher groups
df['Send Time'] = pd.to_datetime(df['Send Time'])
df['DayOfWeek'] = df['Send Time'].dt.day_name()
day_counts = df['DayOfWeek'].value_counts()
print("Messages sent on each day of the week:")
print(day_counts)

#find out the line or a word most used in a group
message_counts = df['Message'].value_counts()
most_used_line = message_counts.idxmax()
count_of_most_used = message_counts.max()
print(f"The most used line in the group is '{most_used_line}' with {count_of_most_used} occurrences.")

# frequent participants in the group
sender_message_counts = df.groupby('Sender ID').size()
most_frequent_sender_id = sender_message_counts.idxmax()
count_of_most_messages = sender_message_counts.max()
print(f"The most frequent participant in the group (by messages sent) is Sender ID: {most_frequent_sender_id} with {count_of_most_messages} messages sent.")

#find the most common types of dialogs
dialog_type_counts = df['Dialog Type'].value_counts()
most_common_dialog_type = dialog_type_counts.idxmax()
count_of_most_common = dialog_type_counts.max()
print(f"The most common dialog type in the group is '{most_common_dialog_type}' with {count_of_most_common} occurrences.")

#find the dialogs which have the most conversation
dialog_message_counts = df.groupby('Dialog Name')['Message'].count()
most_conversation_dialog = dialog_message_counts.idxmax()
count_of_messages = dialog_message_counts.max()
print(f"The dialog with the most conversation is '{most_conversation_dialog}' with {count_of_messages} messages exchanged.")

# message frequency of specific senders changes over time
df['Send Time'] = pd.to_datetime(df['Send Time'])
sender_message_counts = df.groupby(['Sender ID', df['Send Time'].dt.date])['Message'].count()
sender_message_counts = sender_message_counts.reset_index(name='Message Count')
specific_sender_id = 123456789
sender_data = sender_message_counts[sender_message_counts['Sender ID'] == specific_sender_id]
plt.figure(figsize=(10, 6))
plt.plot(sender_data['Send Time'], sender_data['Message Count'], marker='o', linestyle='-', color='b')
plt.title(f"Message Frequency Over Time for Sender ID: {specific_sender_id}")
plt.xlabel("Date")
plt.ylabel("Number of Messages")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#count of message
total_messages = df['Message'].count()
print(f"The total number of messages in the dataset is: {total_messages}")

#top 10 senders name
sender_message_counts = df.groupby('Sender Name')['Message'].count()
top_10_senders = sender_message_counts.sort_values(ascending=False).head(10)
print("Top 10 Senders by Number of Messages:")
print(top_10_senders)

#count of sender name
sender_message_counts = df['Sender Name'].value_counts()
print("Count of messages sent by each sender:")
print(sender_message_counts)

#time of the day mos activity in the group
df['Hour'] = df['Send Time'].dt.hour
hourly_activity = df['Hour'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(hourly_activity.index, hourly_activity.values, marker='o', linestyle='-', color='b')
plt.title('Message Activity by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Messages')
plt.xticks(range(24))
plt.grid(True)
plt.tight_layout()
plt.show()


# see the most new members joining the group
new_member_events = df[df['Message'].str.contains('joined the group', case=False)]
new_member_events['Join Date'] = new_member_events['Send Time'].dt.date
new_members_by_date = new_member_events['Join Date'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(new_members_by_date.index, new_members_by_date.values, marker='o', linestyle='-', color='b')
plt.title('Trend of New Members Joining the Group')
plt.xlabel('Date')
plt.ylabel('Number of New Members')
plt.grid(True)
plt.tight_layout()
plt.show()

# total number of columns
total_columns = len(df.columns)
print(f'Total number of columns in the dataset: {total_columns}')











