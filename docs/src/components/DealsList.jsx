import React, { useState, useEffect } from "react";
import axios from 'axios';
import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../theme";
// import { DealsListData as data } from "../data/mockData";
import Header from "../components/Header";
import { useTheme } from "@mui/material";

const Contacts = ({ isCustomLineColors = false, isDashboard = false }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [data, setData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
        const response = await axios.get('/api/v1/dealsList/');
        setData(response.data);
        console.log(response.data)
      
    };
  
    fetchData();
  }, []);

  const handlePageChange = (event, value) => {
    setCurrentPage(value);
  };


  const columns = [
    { field: "amount", headerName: "amount", flex: 1 },
    { field: "company", headerName: "company", type: "number", headerAlign: "left", align: "left", flex: 1 },
    { field: "company_slug", headerName: "company_slug", flex: 1 },
    { field: "created_at", headerName: "created_at", flex: 1 },
    { field: "email", headerName: "email", flex: 1 },
    { field: "funding_round", headerName: "funding_round", flex: 1 },
    { field: "id", headerName: "ID", flex: 0.5 },
    { field: "investors", headerName: "investors", flex: 1 },
    { field: "publish", headerName: "publish", flex: 1 },
    { field: "source", headerName: "source", flex: 1 },
    { field: "updated_at", headerName: "updated_at", flex: 1 },
    { field: "user_id", headerName: "user_id", flex: 1 },
    { field: "valuation_note", headerName: "valuation_note", flex: 1 },
    { field: "when", headerName: "when", flex: 1, cellClassName: "when-column--cell" },
  ];

  return (
    <Box m="1px">
      <Header
        title="Deals list"
        subtitle="Deals List for your Reference"
      />
      <Box
        m="5px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          rows={data}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>

      <Box>
          <Pagination
            count={10} // Replace with the actual total number of pages
            page={currentPage}
            onChange={handlePageChange}
          />
      </Box>
    </Box>
  );
};

export default Contacts;
