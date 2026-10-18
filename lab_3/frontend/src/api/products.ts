import type { Product } from "@/types/product";
import { apiClient } from "./client";

export async function getProducts(): Promise<Product[]> {
  const response = await apiClient.get<Product[]>("/products/");
  return response.data;
}

export async function getProductById(id: number): Promise<Product> {
  const response = await apiClient.get<Product>(`/products/${id}/`);
  return response.data;
}
