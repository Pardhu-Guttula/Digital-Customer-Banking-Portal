import React from "react";
import { useIntl } from "react-intl";

import SectionHeader from "./SectionHeader";
import ProductCard from "./ProductCard";

export default function ProductsForYouSection({
  title,
  products = [],
  onViewAll = () => {},
  onApply = () => {},
  hiddenImages = [],
}) {
  const intl = useIntl();

  return (
    <section className="w-full bg-white py-0">
      <div className="mx-auto w-full max-w-[1192px] px-4 sm:px-6 lg:px-0">
        <div className="flex flex-col gap-3">
          <SectionHeader title={title} onViewAll={onViewAll} />

          <div className="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-3">
            {products.map((p) => (
              <ProductCard
                key={p.id}
                {...p}
                onCta={onApply}
                ctaAriaLabel={intl.formatMessage(
                  { id: "productsForYou.applyAriaLabel" },
                  { ctaLabel: p.ctaLabel, title: p.title }
                )}
              />
            ))}
          </div>
        </div>
      </div>

      {hiddenImages.map((src) => (
        <img key={src} src={src} alt="" className="hidden" />
      ))}
    </section>
  );
}