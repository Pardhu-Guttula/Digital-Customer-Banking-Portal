import React from "react";
import { useIntl } from "react-intl";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconTone,
  badgeText,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel = ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[20px]">
      <div className="flex items-start justify-between">
        <IconTile tone={iconTone} icon={icon} />
        <BadgePill text={badgeText} />
      </div>

      <div className="mt-[10px]">
        <h3 className="text-[18px] font-medium leading-[26px] tracking-[-0.4395px] text-[#0A0A0A]">
          {title}
        </h3>
        <p className="mt-[4px] text-[14px] font-normal leading-[20px] tracking-[-0.2px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-[14px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}