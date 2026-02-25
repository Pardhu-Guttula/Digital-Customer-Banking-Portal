import React from "react";
import { useIntl } from "react-intl";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconBg,
  iconColor,
  badgeText,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel =
    ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex h-full flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[24px]">
      <div className="flex items-start justify-between">
        <IconTile icon={icon} bgColor={iconBg} iconColor={iconColor} ariaLabel={`${title} icon`} />
        <BadgePill text={badgeText} />
      </div>

      <div className="mt-[14px]">
        <h3 className="text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0a0a0a]">
          {title}
        </h3>
        <p className="mt-[6px] text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-auto pt-[24px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}