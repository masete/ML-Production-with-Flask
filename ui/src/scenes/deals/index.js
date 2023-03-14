import { Box, Grid, Paper  } from "@mui/material";
// import { Grid, Paper } from '@material-ui/core';
import Header from "../../components/Header";
// import LineChart from "../../components/LineChart";
import DealsLineChart from "../../components/DealsLineChart";

const LineChart = () => {
  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <Paper>Row 1</Paper>
      </Grid>
      <Grid item xs={12}>
        <Paper>Row 2</Paper>
      </Grid>
      <Grid item xs={12}>
        <Paper style={{ backgroundColor: 'transparent' }}>
            <Box m="1px">
              <Header title="Number of deals by year" subtitle="Simple Line Chart" />
              <Box height="75vh">
                <DealsLineChart />
            </Box>
           </Box>
        </Paper>
      </Grid>
      <Grid item xs={12}>
        <Paper>Row 4</Paper>
      </Grid>
      <Grid item xs={12}>
        <Paper>Row 5</Paper>
      </Grid>
    </Grid>
    // <Box m="20px">
    //   <Header title="Number of deals by year" subtitle="Simple Line Chart" />
    //   <Box height="75vh">
    //     <DealsLineChart />
    //   </Box>
    // </Box>
  );
};

export default LineChart;
