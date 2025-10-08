import ErrorPage from "./ErrorPage";
import MyProfile from "./MyProfile";
import Profiles from "./Profiles";
import SingleProfile from "./SingleProfile";
import Home from "./Home";
import About from "./About";

export const routes = [
  {
    path: "/",
    element: <Home></Home>,
  },
  {
    path: "/about",
    element: <About></About>,
  },
  {
    path: "/profiles/",
    element: <Profiles></Profiles>,
    children: [
      {
        path: ":id",
        element: <SingleProfile></SingleProfile>,
      },
      {
        path: "me",
        element: <MyProfile></MyProfile>,
      },
    ],
  },
  {
    path: "*",
    element: <ErrorPage></ErrorPage>,
  },
];