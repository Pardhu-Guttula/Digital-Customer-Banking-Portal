import React from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function PrimaryButton({ children, disabled, onClick = noop }) {
  useIntl();

  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={onClick}
      className="h-11 w-full rounded-lg bg-[#030213] text-sm font-medium leading-5 tracking-[-0.1504px] text-white shadow-sm transition hover:bg-[#07062a] disabled:cursor-not-allowed disabled:opacity-60"
    >
      {children}
    </button>
  );
}