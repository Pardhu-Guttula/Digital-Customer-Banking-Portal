import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/d782a235-cca7-4278-8e00-ff5e8c66c42d";

export default function BrandHeader({
  title,
  subtitle,
  onBrandClick = () => {},
  useRemoteIcon = false,
}) {
  const intl = useIntl();

  return (
    <div style={styles.brandHeader}>
      <button
        type="button"
        onClick={onBrandClick}
        style={styles.brandIconButton}
        aria-label={intl.formatMessage({ id: "brandHeader.brandButtonAriaLabel" })}
      >
        <span style={styles.brandIconBox}>
          {useRemoteIcon ? (
            <img alt="" src={imgIcon} style={styles.brandIconImg} />
          ) : (
            <Landmark size={32} color="#FFFFFF" aria-hidden="true" />
          )}
        </span>
      </button>

      <h1 style={styles.brandTitle}>{title}</h1>
      <p style={styles.brandSubtitle}>{subtitle}</p>
    </div>
  );
}

const styles = {
  brandHeader: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    textAlign: "center",
  },

  brandIconButton: {
    appearance: "none",
    border: "none",
    background: "transparent",
    padding: 0,
    cursor: "pointer",
  },

  brandIconBox: {
    width: 64,
    height: 64,
    borderRadius: 16,
    background: "#155DFC",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    boxShadow: "0 1px 0 rgba(0,0,0,0.02)",
  },

  brandIconImg: {
    width: 32,
    height: 32,
    display: "block",
  },

  brandTitle: {
    margin: 0,
    color: "#101828",
    fontSize: 30,
    lineHeight: "36px",
    fontWeight: 700,
    letterSpacing: "0.3955px",
  },

  brandSubtitle: {
    margin: 0,
    color: "#4A5565",
    fontSize: 16,
    lineHeight: "24px",
    fontWeight: 400,
    letterSpacing: "-0.3125px",
  },
};