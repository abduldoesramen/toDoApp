import * as React from "react";
import { useState } from "react";
import { Fragment } from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import { Link } from "react-router-dom";

// Form default empty values:
const defaultValues = {
  email: "",
  password: "",
};

const SignIn = () => {
  const [showPassword, setShowPassword] = React.useState(false);
  const [formValues, setFormValues] = useState(defaultValues);

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
  };

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };
  return (
    <Fragment>
      <form onSubmit={handleSubmit}>
        <Grid container alignItems="center" justify="center" direction="column">
          <Grid item>
            <h1>Sign In</h1>
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
              type="text"
              value={formValues.password}
              onChange={handleChange}
            />
          </Grid>
          {/* Right now, no checks are being run on this button */}
          <Link to="/home">
            <Button variant="contained" type="submit">
              Sign In
            </Button>
          </Link>
        </Grid>
      </form>
    </Fragment>
  );
};

export default SignIn;
