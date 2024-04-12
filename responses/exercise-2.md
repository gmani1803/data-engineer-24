# Exercise 2

## Business Process Description

Fact Table: GymCheckIns

checkin_id (Primary Key): A unique identifier for each check-in event.
member_id (Foreign Key to Members dimension): Identifies the member checking in.
checkin_datetime: Date and time when the check-in occurred.
checkin_location_id (Foreign Key to Locations dimension): Identifies the gym location where the check-in took place.
checkin_duration_minutes: Duration of the check-in session in minutes.
checkin_type: Type of check-in (e.g., regular check-in, guest check-in, event check-in).
checkin_activity_id (Foreign Key to Activities dimension): Identifies the specific activity or class the member checked in for.
checkin_trainer_id (Foreign Key to Trainers dimension): Identifies the trainer (if applicable) who conducted the activity or class.
Dimensions:

Members Dimension:

member_id (Primary Key): Unique identifier for each gym member.
member_name: Name of the gym member.
member_type: Type of membership (e.g., standard, premium).
member_join_date: Date when the member joined the gym.
member_status: Current status of the membership (e.g., active, suspended, expired).
Locations Dimension:

location_id (Primary Key): Unique identifier for each gym location.
location_name: Name or code of the gym location.
location_address: Physical address of the gym location.
location_city: City where the gym location is situated.
location_state: State or province where the gym location is situated.
location_country: Country where the gym location is situated.
Activities Dimension:

activity_id (Primary Key): Unique identifier for each activity or class.
activity_name: Name of the activity or class.
activity_type: Type of activity (e.g., climbing, yoga, fitness).
activity_duration_minutes: Duration of the activity or class in minutes.
activity_level: Difficulty level of the activity (e.g., beginner, intermediate, advanced).
Trainers Dimension:

trainer_id (Primary Key): Unique identifier for each trainer.
trainer_name: Name of the trainer.
trainer_specialty: Specialty or expertise of the trainer (e.g., climbing instructor, yoga teacher, fitness coach).
trainer_experience_years: Years of experience as a trainer.
trainer_certification: Certification(s) held by the trainer.
This fact table and associated dimensions can effectively model the process of members checking in to the gym, capturing details such as member information, check-in location, check-in activities, and trainer involvement.v
## Fact Table

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |

## Dimension

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |
