import { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/health`)
      .then((response) => response.json())
      .then((data) => console.log(data));
  }, []);
  return (
    <>
      <main className="min-h-screen">
        <div className="mx-auto max-w-7xl px-6 py-10">
          <h1 className="text-3xl font-bold">E-Commerce</h1>
          <p className="mt-2 text-muted-foreground">FastAPI + React</p>
        </div>
      </main>
    </>
  );
}

export default App;
