import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../theme";
import { DealsListData } from "../data/mockData";
import Header from "../components/Header";
import { useTheme } from "@mui/material";

const Contacts = ({ isCustomLineColors = false, isDashboard = false }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const columns = [
    { field: "id", headerName: "ID", flex: 0.5 },
    // { field: "registrarId", headerName: "Registrar ID" },
    {
      field: "DATE",
      headerName: "DATE",
      flex: 1,
      cellClassName: "DATE-column--cell",
    },
    {
      field: "COMPANYNAME",
      headerName: "COMPANYNAME",
      type: "number",
      headerAlign: "left",
      align: "left",
    },
    {
      field: "AMOUNT",
      headerName: "AMOUNT",
      flex: 1,
    },
    {
      field: "ROUND",
      headerName: "ROUND",
      flex: 1,
    },
    {
      field: "INVESTORS",
      headerName: "INVESTORS",
      flex: 1,
    },
    {
      field: "COUNTRY",
      headerName: "COUNTRY",
      flex: 1,
    },
    {
      field: "COUNTRYHQ",
      headerName: "COUNTRYHQ",
      flex: 1,
    },
    {
        field: "CATEGORY",
        headerName: "CATEGORY",
        flex: 1,
    },
    {
        field: "SECTOR",
        headerName: "SECTOR",
        flex: 1,
    },
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
          rows={DealsListData}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );
};

export default Contacts;
