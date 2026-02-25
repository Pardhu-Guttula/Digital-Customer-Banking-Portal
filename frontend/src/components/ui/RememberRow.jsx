import React from "react";
import { useIntl } from "react-intl";

export default function RememberRow({
  remember = false,
  onRememberChange = () => {},
  onForgotPassword = () => {},
}) {
  const intl = useIntl();

  return (
    <div className="flex w-full items-center justify-between gap-4">
      <label className="flex items-center gap-2 text-[16px] font-medium leading-6 tracking-[-0.3125px] text-[#4a5565]">
        <input
          type="checkbox"
          checked={remember}
          onChange={(e) => onRememberChange(e.target.checked)}
          className="h-[13px] w-[13px] rounded-[3px] border border-[#cbd5e1] bg-white align-middle accent-[#155dfc] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/25"
        />
        {intl.formatMessage({ id: "rememberRow.rememberMe" })}
      </label>

      <button
        type="button"
        onClick={onForgotPassword}
        className="text-[14px] leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/25"
      >
        {intl.formatMessage({ id: "rememberRow.forgotPassword" })}
      </button>
    </div>
  );
}