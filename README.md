# medical-backend-py

Django RESTful API:

/


# app.get("/patients", PatientCtrl.all);
**app.post("/patients", patientValidation.create, PatientCtrl.create);**
app.delete("/patients/:id", PatientCtrl.remove);
app.patch("/patients/:id", patientValidation.update, PatientCtrl.update);
app.get("/patients/:id", PatientCtrl.show);

app.get("/appointments", AppointmentCtrl.all);
app.post("/appointments", appointmentValidation.create, AppointmentCtrl.create);
app.delete("/appointments/:id", AppointmentCtrl.remove);
app.patch(
  "/appointments/:id",
  appointmentValidation.update,
  AppointmentCtrl.update
);

app.get("/messages", MessageCtrl.all);
app.post("/messages", MessageCtrl.create);
