# Exercise 2

## Business Process Description
We are implementing a dimensional modeling approach to represent the process of gym check-ins. The fact table "GymCheckIns" serves as the central entity, capturing key metrics such as check-in ID, member ID, check-in date and time, check-in location ID, check-in duration, check-in type, activity ID, and trainer ID.
The associated dimensions include "Members," "Locations," "Activities," and "Trainers," each providing detailed attributes related to gym membership, gym locations, activities/classes offered, and trainer information, respectively.
By linking these dimensions to the fact table through foreign keys, we establish a relational structure that allows for in-depth analysis of member behavior, location performance, activity popularity, and trainer effectiveness. This technical implementation enables efficient data retrieval and analytics, facilitating informed decision-making and optimization of gym operations.
## Fact Table

| Column Name           | Type    | Description                                                   |
|-----------------------|---------|---------------------------------------------------------------|
| checkin_id            | Primary Key | A unique identifier for each check-in event.                 |
| member_id             | Foreign Key | Identifies the member checking in.                            |
| checkin_datetime      | datetime | Date and time when the check-in occurred.                     |
| checkin_location_id   | Foreign Key | Identifies the gym location where the check-in took place.    |
| checkin_duration_minutes | int     | Duration of the check-in session in minutes.                  |
| checkin_type          | varchar | Type of check-in (e.g., regular check-in, guest check-in, event check-in). |
| checkin_activity_id   | Foreign Key | Identifies the specific activity or class the member checked in for. |
| checkin_trainer_id    | Foreign Key | Identifies the trainer (if applicable) who conducted the activity or class. |

## Dimension

# Members Dimension:

| Column Name      | Type    | Description                                             |
|------------------|---------|---------------------------------------------------------|
| member_id        | Primary Key | Unique identifier for each gym member.              |
| member_name      | varchar | Name of the gym member.                               |
| member_type      | varchar | Type of membership (e.g., standard, premium).         |
| member_join_date | date    | Date when the member joined the gym.                  |
| member_status    | varchar | Current status of the membership (e.g., active, suspended, expired). |

# Locations Dimension:

| Column Name         | Type    | Description                                                  |
|---------------------|---------|--------------------------------------------------------------|
| location_id         | Primary Key | Unique identifier for each gym location.               |
| location_name       | varchar | Name or code of the gym location.                      |
| location_address    | varchar | Physical address of the gym location.                  |
| location_city       | varchar | City where the gym location is situated.              |
| location_state      | varchar | State or province where the gym location is situated. |
| location_country    | varchar | Country where the gym location is situated.           |

# Activities Dimension:

| Column Name              | Type    | Description                                                     |
|--------------------------|---------|-----------------------------------------------------------------|
| activity_id              | Primary Key | Unique identifier for each activity or class.              |
| activity_name            | varchar | Name of the activity or class.                            |
| activity_type            | varchar | Type of activity (e.g., climbing, yoga, fitness).         |
| activity_duration_minutes| int     | Duration of the activity or class in minutes.             |
| activity_level           | varchar | Difficulty level of the activity (e.g., beginner, intermediate, advanced). |

# Trainers Dimension:

| Column Name                | Type    | Description                                                          |
|----------------------------|---------|----------------------------------------------------------------------|
| trainer_id                 | Primary Key | Unique identifier for each trainer.                               |
| trainer_name               | varchar | Name of the trainer.                                              |
| trainer_specialty          | varchar | Specialty or expertise of the trainer (e.g., climbing instructor, yoga teacher, fitness coach). |
| trainer_experience_years   | int     | Years of experience as a trainer.                                 |
| trainer_certification      | varchar | Certification(s) held by the trainer.                             |

