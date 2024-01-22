function SidebarContainer({ children }) {
  return (
    <div style={{ display: 'flex', height: '100%' }}>
      <div>
        <h1>SideBar</h1>
      </div>
      {children}
    </div>
  );
}

/**
 * Higher Order Functions that takes a component and returns a new component wrapped with SidebarContainer.
 */
const withSidebar = (Component) => {
  // This HOC returns a new functional component that wraps the provided component (Component) with SidebarContainer.
  return (props) => (
    <SidebarContainer>
      <Component {...props} />
    </SidebarContainer>
  );
};

/**
 * Functional component representing the main activity routes.
 */
const ActivityRoutes = () => {
  // Assuming the usage of Redux useSelector to get data from the state.
  const user = useSelector((state) => state.authReducer.user);
  const isLoadingIdeationBoards = useSelector(
    (state) => state.contentReducer.isLoadingIdeationBoards
  );
  const renderRoutes = () => {
    if (user.is_student) {
      return getRoutes(STUDENT_ACTIVITY_ROUTES);
    } else if (user.is_studio) {
      return getRoutes(STUDIO_ACTIVITY_ROUTES);
    } else {
      return getRoutes(BRAND_ACTIVITY_ROUTES);
    }
  };

  return (
    <LoadingContainer loading={isLoadingIdeationBoards}>
      <Routes>
        <Route path='' element={<MyActivity />} />
        {renderRoutes()}
      </Routes>
    </LoadingContainer>
  );
};

// Applying the withSidebar Higher Order Function to the ActivityRoutes component.
export default withSidebar(ActivityRoutes);
