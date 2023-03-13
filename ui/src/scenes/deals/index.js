import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import { yVposts } from "../../data/yearVposts";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";
import PieChart from "../../components/PieChart";

const Deals = () => {
    return (
        <Box m="20px">
          <Header title="Pie Chart" subtitle="Simple Pie Chart" />
          <Box height="75vh">
            <PieChart />
          </Box>
        </Box>
      );
    };
  
  export default Deals;
  