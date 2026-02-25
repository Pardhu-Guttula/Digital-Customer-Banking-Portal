import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/82e0ea7f-9068-4ba5-a8c2-c44d6446c24e";
const imgVector = "https://www.figma.com/api/mcp/asset/e1d69046-0a4e-412d-bd45-8a34505cf0cd";
const imgVector1 = "https://www.figma.com/api/mcp/asset/65d0517b-770c-4009-a86f-57052d2cdecf";
const imgVector2 = "https://www.figma.com/api/mcp/asset/bc5d30f2-1fdf-4e82-9649-0eb24c573330";
const imgVector3 = "https://www.figma.com/api/mcp/asset/7355a83d-016c-4c2b-9e3b-2abd154a973c";
const imgVector4 = "https://www.figma.com/api/mcp/asset/56d49047-3672-46d0-bf64-5f0d97718445";
const imgVector5 = "https://www.figma.com/api/mcp/asset/bf4c86fa-ce9c-48a6-8302-4216db930d64";
const imgVector6 = "https://www.figma.com/api/mcp/asset/b1616efe-ca18-4848-b881-7f2e3df3b164";

export default function ProductsForYou({
  title,
  actionLabel,
  onViewAll = () => {},
  products,
  onApply = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "productsForYou.title" });
  const resolvedActionLabel = actionLabel ?? intl.formatMessage({ id: "productsForYou.viewAll" });

  const resolvedProducts =
    products ??
    [
      {
        id: "premium-savings",
        icon: PiggyBank,
        iconTone: "green",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.recommended" }),
        title: intl.formatMessage({ id: "productsForYou.product.premiumSavings.title" }),
        description: intl.formatMessage({ id: "productsForYou.product.premiumSavings.description" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "personal-loan",
        icon: TrendingUp,
        iconTone: "blue",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.preApproved" }),
        title: intl.formatMessage({ id: "productsForYou.product.personalLoan.title" }),
        description: intl.formatMessage({ id: "productsForYou.product.personalLoan.description" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconTone: "purple",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.limitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.product.goldCreditCard.title" }),
        description: intl.formatMessage({ id: "productsForYou.product.goldCreditCard.description" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ];

  return (
    <section aria-label={resolvedTitle} className="w-full">
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-[16px] px-4 sm:px-6 lg:px-0">
        <SectionHeader title={resolvedTitle} actionLabel={resolvedActionLabel} onAction={onViewAll} />

        <div className="grid grid-cols-1 items-start gap-[16px] md:grid-cols-2 lg:grid-cols-3">
          {resolvedProducts.map((p) => (
            <ProductCard
              key={p.id}
              icon={p.icon}
              iconTone={p.iconTone}
              badgeText={p.badgeText}
              title={p.title}
              description={p.description}
              ctaLabel={p.ctaLabel}
              onCta={() => onApply(p.id)}
            />
          ))}
        </div>

        <div className="sr-only">
          <img alt="" src={imgIcon} />
          <img alt="" src={imgVector} />
          <img alt="" src={imgVector1} />
          <img alt="" src={imgVector2} />
          <img alt="" src={imgVector3} />
          <img alt="" src={imgVector4} />
          <img alt="" src={imgVector5} />
          <img alt="" src={imgVector6} />
        </div>
      </div>
    </section>
  );
}