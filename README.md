# medical-backend-py

# Django RESTful API:
**/login -- POST(username, password)**

**/register -- POST(username, password, password_confirmation, email)**

**/register_person -- POST(user_id, name, surname, dob, gender, phone)**

**/register_patient -- POST(user_id, info)**

**/register_doctor -- POST(user_id, clinic_id, speciality)**

**/register_patient_doctor -- POST(user_id, doctor_id)**

**/register_clinic -- POST(user_id, name, city, address, phone)**

**/clinic -- GET, POST(user_id, clinic_id, name, city, address, phone)**

**/doctor -- GET(clinic_id), GET(doctor_id)**


