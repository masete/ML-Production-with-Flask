import React, { useState } from 'react';
import { Box, Button, TextField } from "@mui/material";
import { Formik } from "formik";
import * as yup from "yup";
import useMediaQuery from "@mui/material/useMediaQuery";
import Header from "../../components/Header";

const Predict = () => {
  const isNonMobile = useMediaQuery("(min-width:600px)");

  const [isloading, setIsloading] = useState(false)
  const [result, setResult] = useState("");

  const [values, setValues] = useState({
    Last_funding_round_raised_amount: "",
    age_of_company: "",
    Amount_of_the_last_funding_type: "",
    Companies_Information_Level_of_Completeness: "",
    Stage_DA_Classified_Early: "",
    number_of_founders: "",
    number_of_bussiness_categories: "",
    number_of_market_countires: "",
    Female_Co_Founder: "",
    Average_time_of_rounds: "",
    number_of_investors: 0,
    Sector_Information_Technology: "",
    Business_model_B2C: ""

});

  const handleChange = (e, changeKey=undefined) => {
  // console.log(changeKey, e.target.value)
  let newData = {...values}
  if(changeKey) {
      newData[changeKey] = e.target.value
  }
  else newData[e.target.id] = e.target.value
  setValues(newData)

}

  const handleClick = (event) => {
  //const proxyurl = "https://salty-reaches-05509.herokuapp.com/";
  
  const url = "http://127.0.0.1:42707/predict/";

    setIsloading(true);
    fetch(url,
    {
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(values)
    })  //https://salty-reaches-05509.herokuapp.com/http://127.0.0.1:5000/prediction
    .then(response => response.json())
    .then(response => {
        setResult(response.result);
        setIsloading(false);
    });
};


  const handleFormSubmit = (values) => {
    console.log(values);
  };

  return (
    <Box m="20px">
      <Header title="Predict" subtitle="Predicting the probability in reaching series A financing" />

      <Formik
        onSubmit={handleFormSubmit}
        onChange={handleChange}
        initialValues={initialValues}
        validationSchema={checkoutSchema}
      >
        {({
          values,
          errors,
          touched,
          handleBlur,
          handleChange,
          handleSubmit,
        }) => (
          <form onSubmit={handleSubmit}>
            <Box
              display="grid"
              gap="30px"
              gridTemplateColumns="repeat(4, minmax(0, 1fr))"
              sx={{
                "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
              }}
            >
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="16_Last funding round raised amount"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Last_funding_round_raised_amount}
                name="firstName"
                error={!!touched.firstName && !!errors.firstName}
                helperText={touched.firstName && errors.firstName}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="age_of_company"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.age_of_company}
                name="lastName"
                error={!!touched.lastName && !!errors.lastName}
                helperText={touched.lastName && errors.lastName}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Amount of the last funding type"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Amount_of_the_last_funding_type}
                name="email"
                error={!!touched.lastName && !!errors.lastName}
                helperText={touched.lastName && errors.lastName}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Companies Information, Level of Completeness"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Companies_Information_Level_of_Completeness}
                name="contact"
                error={!!touched.lastName && !!errors.lastName}
                helperText={touched.lastName && errors.lastName}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Stage, DA Classified_Early"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Stage_DA_Classified_Early}
                name="address1"
                error={!!touched.address1 && !!errors.address1}
                helperText={touched.address1 && errors.address1}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="number of founders"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.number_of_founders}
                name="address2"
                error={!!touched.address2 && !!errors.address2}
                helperText={touched.address2 && errors.address2}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="number of bussiness categories"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.number_of_bussiness_categories}
                name="address1"
                error={!!touched.address1 && !!errors.address1}
                helperText={touched.address1 && errors.address1}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="number of market countires"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.number_of_market_countires}
                name="address2"
                error={!!touched.address2 && !!errors.address2}
                helperText={touched.address2 && errors.address2}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Female_Co-Founder"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Female_Co_Founder}
                name="address1"
                error={!!touched.address1 && !!errors.address1}
                helperText={touched.address1 && errors.address1}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Average time of rounds(days)"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Average_time_of_rounds}
                name="address2"
                error={!!touched.address2 && !!errors.address2}
                helperText={touched.address2 && errors.address2}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="number of investors"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.number_of_investors}
                name="address2"
                error={!!touched.address2 && !!errors.address2}
                helperText={touched.address2 && errors.address2}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Sector_Information Technology"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Sector_Information_Technology}
                name="address1"
                error={!!touched.address1 && !!errors.address1}
                helperText={touched.address1 && errors.address1}
                sx={{ gridColumn: "span 2" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Business_model_B2C"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.Business_model_B2C}
                name="address1"
                error={!!touched.address1 && !!errors.address1}
                helperText={touched.address1 && errors.address1}
                sx={{ gridColumn: "span 2" }}
              />
            </Box>
            <Box display="flex" justifyContent="end" mt="20px">
              <Button onClick={()=>handleClick()} type="submit" color="secondary" variant="contained">
                Predict
              </Button>
            </Box>
          </form>
        )}
      </Formik>
    </Box>
  );
};

const phoneRegExp =
  /^((\+[1-9]{1,4}[ -]?)|(\([0-9]{2,3}\)[ -]?)|([0-9]{2,4})[ -]?)*?[0-9]{3,4}[ -]?[0-9]{3,4}$/;

const checkoutSchema = yup.object().shape({
  firstName: yup.string().required("required"),
  lastName: yup.string().required("required"),
  email: yup.string().email("invalid email").required("required"),
  contact: yup
    .string()
    .matches(phoneRegExp, "Phone number is not valid")
    .required("required"),
  address1: yup.string().required("required"),
  address2: yup.string().required("required"),
});
const initialValues = {
  firstName: "",
  lastName: "",
  email: "",
  contact: "",
  address1: "",
  address2: "",
};

export default Predict;
