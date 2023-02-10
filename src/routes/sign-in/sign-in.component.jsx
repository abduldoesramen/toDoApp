import * as React from "react";
import { useState, useEffect } from "react";
import { Fragment } from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import { useNavigate } from "react-router-dom";

// Form default empty values:
const defaultValues = {
  email: "",
  password: "",
};

const SignIn = () => {
  const [formValues, setFormValues] = useState(defaultValues);
  const [currentTime, setCurrentTime] = useState(1);
  const [currentUser, setCurrentUser] = useState();
  let navigate = useNavigate();

  // From flask, empty array for no dependency spam updating with time changes
  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
      });
  }, []);

  useEffect(() => {
    fetch("/users")
      .then((res) => res.json())
      .then((data) => {
        setCurrentUser(data.count);
      });
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(formValues);
    navigate("/home");
  };

  return (
    <Fragment>
      <form onSubmit={handleSubmit}>
        <Grid container alignItems="center" justify="center" direction="column">
          <Grid item>
            <h1>Sign In</h1>
            <p>{currentTime}</p>
          </Grid>
          <Grid item marginTop={2}>
            <TextField
              id="email-input"
              name="email"
              label="Email"
              value={formValues.email}
              onChange={handleChange}
            />
          </Grid>
          <Grid item marginTop={2} marginBottom={2}>
            <TextField
              id="password-input"
              name="password"
              label="Password"
              type="password"
              value={formValues.password}
              onChange={handleChange}
            />
          </Grid>
          {/* Right now, no checks are being run on this button */}
          <Button
            variant="contained"
            type="submit"
            onClick={async () => {
              const information = {
                email: formValues.email,
                password: formValues.password,
              };
              const response = await fetch("/users/generate", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(information),
              });
            }}
          >
            Sign In
          </Button>
        </Grid>
      </form>
    </Fragment>
  );
};

export default SignIn;
