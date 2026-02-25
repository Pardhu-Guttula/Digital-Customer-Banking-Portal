import React from "react";
import { useIntl } from "react-intl";
import ProductCard from "./ProductCard";

export default function ProductCardsGrid({ items }) {
  const intl = useIntl();
  const resolvedItems = items ?? [];

  return (
    <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
      {resolvedItems.map((item) => (
        <ProductCard key={item.id ?? intl.formatMessage({ id: "productCardsGrid.fallbackKey" })} {...item} />
      ))}
    </div>
  );
}