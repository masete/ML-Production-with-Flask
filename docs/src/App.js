import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard";
import Team from "./scenes/team";
// import Deals from "./scenes/deals/PieChart";
import Invoices from "./scenes/invoices";
import Contacts from "./scenes/contacts";
import Company from "./scenes/company";
import Investor from "./scenes/investors";
import Founders from "./scenes/founders";
import Bar from "./scenes/bar";
import CompanyForm from "./scenes/company-form";
import InvestorForm from "./scenes/investor-form";
import FoundersForm from "./scenes/founders-form";
import Form from "./scenes/form";
import Predict from "./scenes/predict";
import PredInvst from "./scenes/predict_investors";
import Line from "./scenes/line";
import DealsLineChart from "./scenes/deals";
import Pie from "./scenes/pie";
import FAQ from "./scenes/faq";
import Geography from "./scenes/geography";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
// import Deals from "./scenes/deals";
// import Calendar from "./scenes/calendar/calendar";

function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar isSidebar={isSidebar} />
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar} />
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/team" element={<Team />} />
              <Route path="/deals" element={<DealsLineChart />} />
              <Route path="/contacts" element={<Contacts />} />
              <Route path="/company" element={<Company />} />
              <Route path="/investors" element={<Investor />} />
              <Route path="/founders" element={<Founders />} />
              <Route path="/invoices" element={<Invoices />} />
              <Route path="/form" element={<Form />} />
              <Route path="/company-form" element={<CompanyForm />} />
              <Route path="/founders-form" element={<FoundersForm />} />
              <Route path="/investor-form" element={<InvestorForm />} />
              <Route path="/predict" element={<Predict />} />
              <Route path="/predict_investors" element={<PredInvst />} />
              <Route path="/bar" element={<Bar />} />
              <Route path="/pie" element={<Pie />} />
              <Route path="/line" element={<Line />} />
              <Route path="/faq" element={<FAQ />} />
              {/* <Route path="/calendar" element={<Calendar />} /> */}
              <Route path="/geography" element={<Geography />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
