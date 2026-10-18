import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import type { Product } from "@/types/product";

interface ProductCardProps {
  product: Product;
}

export function ProductCard({ product }: ProductCardProps) {
  return (
    <Card className="h-full">
      <CardHeader>
        <div className="flex items-start justify-between gap-3">
          <CardTitle className="text-lg">{product.name}</CardTitle>

          <span className="shrink-0 text-sm font-semibold">
            ${product.price.toFixed(2)}
          </span>
        </div>

        <p className="text-sm text-muted-foreground">{product.category.name}</p>
      </CardHeader>

      <CardContent className="space-y-3">
        <p className="line-clamp-3 text-sm">{product.description}</p>

        <p className="text-xs text-muted-foreground">
          {product.reviews.length} reviews
        </p>
      </CardContent>
    </Card>
  );
}
