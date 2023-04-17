import React, { useState } from "react";
import { Box, Button, TextField } from "@mui/material";
import { Formik } from "formik";
import * as yup from "yup";
import useMediaQuery from "@mui/material/useMediaQuery";
import Header from "../../components/Header";
// import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
// import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

const PredInvst = () => {
  const isNonMobile = useMediaQuery("(min-width:600px)");
  const [values, setValues] =useState({})
  const [result, setResult] = useState("")
  // const [response, setResponse] = useState('');
  // const [isLoading, setIsloading] = useState(false);

  const handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    let inputData = {...values};
    inputData[name]=value;
    setValues(inputData);
}


  const handleSubmit = (values, { setSubmitting }) => {

    console.log(values)
    
    fetch("/predict_series_A", {
      method: 'POST',
      body: JSON.stringify(values),
      headers: {
        'Content-Type': 'application/json'
      }
    // })
    // .then(response => {
    //   if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //   }
    //   return response.json();
    })
      .then(response => response.json())
      .then(response => {
        // result: response.result,
        console.log(response.result)
        setResult(response.result)
    })
    .catch(error => {
      // handle the error
    })
    .finally(() => {
      // set the submitting state to false
      setSubmitting(false);
    });
  }


  // const NextForm = ({ result }) => {
  //   return (
  //     <div>
  //       <h2>Results</h2>
  //       <p>Prediction: {result}</p>
  //     </div>
  //   );
  // };
  

  return (
    <Box m="20px">
      <Header title="Predicitng Investors" subtitle="Predicting investors likely to invest in a given startup." />

      <Formik
        // onSubmit={handleFormSubmit}
        initialValues={initialValues}
        onChange={(e)=>handleChange(e)}
        validationSchema={checkoutSchema}
        onSubmit={handleSubmit}
      >
        {({
          values,
          errors,
          touched,
          handleBlur,
          handleChange,
          handleSubmit,
          isSubmitting
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
                label="Deals Information, Level of Completeness"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Last_funding_round_raised_amount}
                name="Last_funding_round_raised_amount"
                error={!!touched.Last_funding_round_raised_amount && !!errors.Last_funding_round_raised_amount}
                helperText={touched.Last_funding_round_raised_amount && errors.Last_funding_round_raised_amount}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Disclosed"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.age_of_company}
                name="age_of_company"
                error={!!touched.age_of_company && !!errors.age_of_company}
                helperText={touched.age_of_company && errors.age_of_company}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Founded"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Amount_of_the_last_funding_type}
                name="Amount_of_the_last_funding_type"
                error={!!touched.Amount_of_the_last_funding_type && !!errors.Amount_of_the_last_funding_type}
                helperText={touched.Amount_of_the_last_funding_type && errors.Amount_of_the_last_funding_type}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Total  Disclosed Funding"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Companies_Information_Level_of_Completeness}
                name="Companies_Information_Level_of_Completeness"
                error={!!touched.Companies_Information_Level_of_Completeness && !!errors.Companies_Information_Level_of_Completeness}
                helperText={touched.Companies_Information_Level_of_Completeness && errors.Companies_Information_Level_of_Completeness}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="DA Classification_African Company (Yes = 0; No = 1)"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Stage_DA_Classified_Early}
                name="Stage_DA_Classified_Early"
                error={!!touched.Stage_DA_Classified_Early && !!errors.Stage_DA_Classified_Early}
                helperText={touched.Stage_DA_Classified_Early && errors.Stage_DA_Classified_Early}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Number of Founders"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.number_of_founders}
                name="number_of_founders"
                error={!!touched.number_of_founders && !!errors.number_of_founders}
                helperText={touched.number_of_founders && errors.number_of_founders}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Year"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.number_of_bussiness_categories}
                name="number_of_bussiness_categories"
                error={!!touched.number_of_bussiness_categories && !!errors.number_of_bussiness_categories}
                helperText={touched.number_of_bussiness_categories && errors.number_of_bussiness_categories}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Month"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.number_of_market_countires}
                name="number_of_market_countires"
                error={!!touched.number_of_market_countires && !!errors.number_of_market_countires}
                helperText={touched.number_of_market_countires && errors.number_of_market_countires}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Month"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Female_Co_Founder}
                name="Female_Co_Founder"
                error={!!touched.Female_Co_Founder && !!errors.Female_Co_Founder}
                helperText={touched.Female_Co_Founder && errors.Female_Co_Founder}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Quarter"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Average_time_of_rounds}
                name="Average_time_of_rounds"
                error={!!touched.Average_time_of_rounds && !!errors.Average_time_of_rounds}
                helperText={touched.Average_time_of_rounds && errors.Average_time_of_rounds}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Half"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.number_of_investors}
                name="number_of_investors"
                error={!!touched.number_of_investors && !!errors.number_of_investors}
                helperText={touched.number_of_investors && errors.number_of_investors}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Number of Investors"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Sector_Information_Technology}
                name="Sector_Information_Technology"
                error={!!touched.Sector_Information_Technology && !!errors.Sector_Information_Technology}
                helperText={touched.Sector_Information_Technology && errors.Sector_Information_Technology}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Main Sector"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Business_model_B2C}
                name="Business_model_B2C"
                error={!!touched.Business_model_B2C && !!errors.Business_model_B2C}
                helperText={touched.Business_model_B2C && errors.Business_model_B2C}
                sx={{ gridColumn: "span 1" }}
              />
              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Funding Round"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Business_model_B2C}
                name="Business_model_B2C"
                error={!!touched.Business_model_B2C && !!errors.Business_model_B2C}
                helperText={touched.Business_model_B2C && errors.Business_model_B2C}
                sx={{ gridColumn: "span 1" }}
              />

              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Country"
                onBlur={handleBlur}
                onChange={(e)=>handleChange(e)}
                value={values.Business_model_B2C}
                name="Business_model_B2C"
                error={!!touched.Business_model_B2C && !!errors.Business_model_B2C}
                helperText={touched.Business_model_B2C && errors.Business_model_B2C}
                sx={{ gridColumn: "span 1" }}
              />
            </Box>
            <Box display="flex" justifyContent="end" mt="20px">
              <Button type="submit" disabled={isSubmitting} color="secondary" variant="contained">
                Predict Series A
              </Button>
            </Box>
          </form>
        )}
      </Formik>

      {/* {response && <p>{response}</p>} */}
      {/* <p>{{response}}</p> */}

      <div>

        {result === "" ? null :
              (
              <Row>
                <p> 
                  {/* className="result-container"> */}
                  <Col>{result}</Col>
                </p>
              </Row>
              )
        }

      </div>
      {/* {result === "" ? null : */}
        {/* <NextForm values={result} /> */}
      {/* } */}
      {/* <div>
      {result ? (
        <ul>
          {result.map(item => (
            <li>{result}</li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div> */}

    </Box>
  );
};

// const phoneRegExp =
//   /^((\+[1-9]{1,4}[ -]?)|(\([0-9]{2,3}\)[ -]?)|([0-9]{2,4})[ -]?)*?[0-9]{3,4}[ -]?[0-9]{3,4}$/;

const checkoutSchema = yup.object().shape({
  Last_funding_round_raised_amount: yup.string().required("required"),
  age_of_company: yup.string().required("required"),
  Amount_of_the_last_funding_type: yup.string().required("required"),
  Companies_Information_Level_of_Completeness: yup.string().required("required"),
  Stage_DA_Classified_Early: yup.string().required("required"),
  number_of_founders: yup.string().required("required"),
  number_of_bussiness_categories: yup.string().required("required"),
  number_of_market_countires: yup.string().required("required"),
  Female_Co_Founder: yup.string().required("required"),
  Average_time_of_rounds: yup.string().required("required"),
  number_of_investors: yup.string().required("required"),
  Sector_Information_Technology: yup.string().required("required"),
  Business_model_B2C: yup.string().required("required"),
  
});
const initialValues = {
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
  number_of_investors: "",
  Sector_Information_Technology: "",
  Business_model_B2C: ""
};

export default PredInvst;
