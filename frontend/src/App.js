import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Login} from './componets/Login';
import {Home} from './componets/Home';
import { Navigation } from './componets/Navigations';
import {Logout} from './componets/Logout';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    return <BrowserRouter>
            <Navigation></Navigation>
            <Routes>
              <Route path="/" element={<Home/>}/>
              <Route path="/login" element={<Login/>}/>
              <Route path="/logout" element={<Logout/>}/>
            </Routes>
          </BrowserRouter>;
}
export default App;