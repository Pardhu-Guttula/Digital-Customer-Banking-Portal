import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCardsGrid from "./ui/ProductCardsGrid";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/0736c0f7-f30c-48cb-a5e0-846747f92833";
const imgVector =
  "https://www.figma.com/api/mcp/asset/d76d0e34-7c4a-4189-8b8e-1b07a623c18c";
const imgVector1 =
  "https://www.figma.com/api/mcp/asset/04795609-9b5e-421d-9123-d8141ec740eb";
const imgVector2 =
  "https://www.figma.com/api/mcp/asset/c59c14ce-0d9f-4be9-b78d-c3354eba06d0";
const imgVector3 =
  "https://www.figma.com/api/mcp/asset/472ebe54-9166-4b9b-ad42-77edeef879c9";
const imgVector4 =
  "https://www.figma.com/api/mcp/asset/03f34b53-3faa-4430-b820-6518ce6b55cf";
const imgVector5 =
  "https://www.figma.com/api/mcp/asset/e749bd36-ac83-4ae0-8ca4-370db6ed2c38";
const imgVector6 =
  "https://www.figma.com/api/mcp/asset/905dfa3e-2a5f-4add-9a69-f0e95e1c8a68";

export default function ProductsForYou({
  title,
  items,
  onViewAll = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "productsForYou.title" });

  const resolvedItems =
    items ??
    [
      {
        id: "savings",
        icon: PiggyBank,
        iconBg: "#f0fdf4",
        iconColor: "#16a34a",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.savingsTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.savingsDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
      {
        id: "loan",
        icon: TrendingUp,
        iconBg: "#eff6ff",
        iconColor: "#2563eb",
        badgeText: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.loanTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.loanDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
      {
        id: "card",
        icon: CreditCard,
        iconBg: "#faf5ff",
        iconColor: "#9333ea",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.cardTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.cardDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
    ];

  return (
    <section className="w-full">
      <div className="flex w-full flex-col gap-[16px]">
        <SectionHeader
          title={resolvedTitle}
          actionLabel={intl.formatMessage({ id: "common.viewAll" })}
          onAction={onViewAll}
        />
        <ProductCardsGrid items={resolvedItems} />
      </div>

      {/* Asset constants preserved from input (not used after converting to lucide-react icons) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgVector} alt="" className="hidden" />
      <img src={imgVector1} alt="" className="hidden" />
      <img src={imgVector2} alt="" className="hidden" />
      <img src={imgVector3} alt="" className="hidden" />
      <img src={imgVector4} alt="" className="hidden" />
      <img src={imgVector5} alt="" className="hidden" />
      <img src={imgVector6} alt="" className="hidden" />
    </section>
  );
}