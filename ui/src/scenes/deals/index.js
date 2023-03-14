import { Box } from "@mui/material";
import Header from "../../components/Header";
// import LineChart from "../../components/LineChart";
import DealsLineChart from "../../components/DealsLineChart";

const LineChart = () => {
  return (
    <Box m="20px">
      <Header title="Line Chart showing year with most deals" subtitle="Simple Line Chart" />
      <Box height="75vh">
        <DealsLineChart />
      </Box>
    </Box>
  );
};

export default LineChart;
