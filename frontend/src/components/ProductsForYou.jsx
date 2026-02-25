import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";

import ProductsForYouSection from "./ui/ProductsForYouSection";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/fc1b6bd3-f60a-44cf-84d3-ef6d9c1f39fb";
const imgVector =
  "https://www.figma.com/api/mcp/asset/8219da40-e6d7-4528-bde8-6014d62e180c";
const imgVector1 =
  "https://www.figma.com/api/mcp/asset/8ac66634-b592-44d5-b186-86fc32f0da54";
const imgVector2 =
  "https://www.figma.com/api/mcp/asset/9f0208bb-ae1d-49f2-946a-aee78273f223";
const imgVector3 =
  "https://www.figma.com/api/mcp/asset/b94d6d13-b5f3-438e-bc44-ddeaa10b6df2";
const imgVector4 =
  "https://www.figma.com/api/mcp/asset/60f54cf9-8d09-4efb-a568-785d0f599ad9";
const imgVector5 =
  "https://www.figma.com/api/mcp/asset/0cb04d8b-b3c8-4988-b99b-95b76e5a77f0";
const imgVector6 =
  "https://www.figma.com/api/mcp/asset/83c80008-7cee-4ced-bcbc-eab48d494e6b";

export default function ProductsForYou() {
  const intl = useIntl();

  const products = [
    {
      id: "premium-savings",
      icon: PiggyBank,
      iconBg: "#f0fdf4",
      iconColor: "#16a34a",
      badgeLabel: intl.formatMessage({
        id: "productsForYou.badge.recommended",
      }),
      title: intl.formatMessage({
        id: "productsForYou.product.premiumSavings.title",
      }),
      description: intl.formatMessage({
        id: "productsForYou.product.premiumSavings.description",
      }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
    {
      id: "personal-loan",
      icon: TrendingUp,
      iconBg: "#eff6ff",
      iconColor: "#2563eb",
      badgeLabel: intl.formatMessage({
        id: "productsForYou.badge.preApproved",
      }),
      title: intl.formatMessage({
        id: "productsForYou.product.personalLoan.title",
      }),
      description: intl.formatMessage({
        id: "productsForYou.product.personalLoan.description",
      }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
    {
      id: "gold-credit-card",
      icon: CreditCard,
      iconBg: "#faf5ff",
      iconColor: "#9333ea",
      badgeLabel: intl.formatMessage({
        id: "productsForYou.badge.limitedOffer",
      }),
      title: intl.formatMessage({
        id: "productsForYou.product.goldCreditCard.title",
      }),
      description: intl.formatMessage({
        id: "productsForYou.product.goldCreditCard.description",
      }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
  ];

  const handleViewAll = () => {};
  const handleApply = () => {};

  return (
    <ProductsForYouSection
      title={intl.formatMessage({ id: "productsForYou.sectionTitle" })}
      products={products}
      onViewAll={handleViewAll}
      onApply={handleApply}
      hiddenImages={[
        imgIcon,
        imgVector,
        imgVector1,
        imgVector2,
        imgVector3,
        imgVector4,
        imgVector5,
        imgVector6,
      ]}
    />
  );
}