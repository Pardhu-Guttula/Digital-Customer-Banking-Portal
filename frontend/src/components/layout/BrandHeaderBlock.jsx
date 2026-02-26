import React from "react";
import { useIntl } from "react-intl";
import BrandMark from "../ui/BrandMark";

export default function BrandHeaderBlock({
  title,
  subtitle,
  onBrandClick = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "brandHeaderBlock.defaultTitle" });
  const resolvedSubtitle =
    subtitle ?? intl.formatMessage({ id: "brandHeaderBlock.defaultSubtitle" });

  return (
    <header
      aria-label={intl.formatMessage({ id: "brandHeaderBlock.ariaLabel" })}
      style={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        gap: 8,
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
      }}
    >
      <BrandMark onClick={onBrandClick} title={resolvedTitle} />

      <h1
        style={{
          margin: 0,
          color: "#101828",
          fontWeight: 700,
          fontSize: 30,
          lineHeight: "36px",
          letterSpacing: "0.3955px",
        }}
      >
        {resolvedTitle}
      </h1>

      <p
        style={{
          margin: 0,
          color: "#4A5565",
          fontWeight: 400,
          fontSize: 16,
          lineHeight: "24px",
          letterSpacing: "-0.3125px",
        }}
      >
        {resolvedSubtitle}
      </p>
    </header>
  );
}