import { Button } from "./components/ui/button";
import { Skeleton } from "./components/ui/skeleton";
import { useProducts } from "./hooks/useProducts";

function App() {
  const {
    data: products,
    isPending,
    isError,
    error,
    refetch,
    isFetching,
  } = useProducts();
  return (
    <>
      <main className="min-h-screen">
        <div className="mx-auto max-w-7xl space-y-6 px-6 py-10">
          <h1 className="text-3xl font-bold">E-Commerce</h1>

          <p className="text-muted-foreground">
            FastAPI + React + TanStack Query
          </p>
          {isPending && (
            <div className="space-y-3">
              <Skeleton className="h-8 w-full" />
              <Skeleton className="h-8 w-full" />
            </div>
          )}
          {isError && (
            <div className="space-y-3">
              <p role="alert" className="text-destructive">
                {error.message}
              </p>
              <Button onClick={() => void refetch()}>Retry</Button>
            </div>
          )}
          {products && (
            <section className="space-y-4">
              <div className="flex items-center gap-4">
                <p>Products loaded: {products.length}</p>
                <Button
                  variant="outline"
                  disabled={isFetching}
                  onClick={() => void refetch()}
                >
                  {isFetching ? "Refreshing..." : "Refresh"}
                </Button>
              </div>
              <ul className="space-y-2">
                {products.map((product) => (
                  <li key={product.id}>
                    {product.name} — ${product.price}
                    <span className="text-muted-foreground">
                      {" "}
                      ({product.category.name})
                    </span>
                  </li>
                ))}
              </ul>
            </section>
          )}
        </div>
      </main>
    </>
  );
}

export default App;
