import { ProductGrid } from "@/components/ProductGrid";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { useProducts } from "@/hooks/useProducts";

export function ProductsPage() {
  const {
    data: products,
    isPending,
    isError,
    error,
    isFetching,
    refetch,
  } = useProducts();

  if (isPending) {
    return (
      <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {Array.from({ length: 6 }).map((_, index) => (
          <Skeleton key={index} className="h-48 w-full" />
        ))}
      </div>
    );
  }

  if (isError) {
    return (
      <section className="space-y-4" role="alert">
        <h2 className="text-xl font-semibold">Unable to load products</h2>

        <p className="text-sm text-destructive">{error.message}</p>

        <Button onClick={() => void refetch()}>Retry</Button>
      </section>
    );
  }

  return (
    <section className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-semibold">Products</h2>

          <p className="text-sm text-muted-foreground">
            {products.length} products available
          </p>
        </div>

        <Button
          variant="outline"
          disabled={isFetching}
          onClick={() => void refetch()}
        >
          {isFetching ? "Refreshing..." : "Refresh"}
        </Button>
      </div>

      {products.length === 0 ? (
        <div className="rounded-lg border border-dashed p-10 text-center">
          <h3 className="font-medium">No products available</h3>

          <p className="mt-2 text-sm text-muted-foreground">
            Products will appear here when they are added.
          </p>
        </div>
      ) : (
        <ProductGrid products={products} />
      )}
    </section>
  );
}
