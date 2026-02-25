import React from "react";
import { useIntl } from "react-intl";
import cx from "../utils/cx";

export default function PrimaryButton({
  children,
  onClick = () => {},
  disabled = false,
  loading = false,
  type = "submit",
}) {
  const intl = useIntl();

  return (
    <button
      type={type}
      disabled={disabled || loading}
      onClick={onClick}
      className={cx(
        "h-11 w-full rounded-lg bg-[#030213] text-white",
        "text-[14px] leading-5 font-medium tracking-[-0.1504px]",
        "hover:bg-[#05051a] active:bg-black",
        "disabled:opacity-60 disabled:cursor-not-allowed",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
      )}
    >
      {loading ? intl.formatMessage({ id: "common.continuing" }) : children}
    </button>
  );
}