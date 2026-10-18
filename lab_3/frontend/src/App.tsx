import { ProductsPage } from "@/pages/ProductsPage";

function App() {
  return (
    <main className="min-h-screen">
      <div className="mx-auto max-w-7xl space-y-8 px-6 py-10">
        <header>
          <h1 className="text-3xl font-bold">E-Commerce</h1>

          <p className="mt-2 text-muted-foreground">
            FastAPI + React + TanStack Query
          </p>
        </header>

        <ProductsPage />
      </div>
    </main>
  );
}

export default App;
