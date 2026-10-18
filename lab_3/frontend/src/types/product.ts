export interface Category {
  id: number;
  name: string;
}

export interface Review {
  id: number;
  text: string;
  rating: number;
  user_id: number;
  product_id: number;
}

export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  category_id: number;
  category: Category;
  reviews: Review[];
}
