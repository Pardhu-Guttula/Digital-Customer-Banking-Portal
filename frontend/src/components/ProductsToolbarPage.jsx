import React, { useState } from "react";
import ProductsToolbar from "./layout/ProductsToolbar";

export default function ProductsToolbarPage() {
  const [sortValue, setSortValue] = useState("");
  const [view, setView] = useState("grid");

  const sortOptions = [
    { value: "featured", label: "Featured" },
    { value: "price_asc", label: "Price: Low to High" },
    { value: "price_desc", label: "Price: High to Low" },
    { value: "newest", label: "Newest" },
  ];

  return (
    <div className="w-full">
      <ProductsToolbar
        shownCount={12}
        totalCount={20}
        sortValue={sortValue}
        sortOptions={sortOptions}
        onSortChange={setSortValue}
        view={view}
        onViewChange={setView}
      />
    </div>
  );
}