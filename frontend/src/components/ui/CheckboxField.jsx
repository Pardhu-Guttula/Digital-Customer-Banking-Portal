import React from "react";
import { useIntl } from "react-intl";
import { Check } from "lucide-react";
import cx from "../utils/cx";

export default function CheckboxField({ checked, onCheckedChange = () => {}, label, id }) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-2">
      <button
        type="button"
        role="checkbox"
        aria-checked={checked}
        aria-label={label}
        onClick={() => onCheckedChange(!checked)}
        className={cx(
          "h-[13px] w-[13px] rounded-[3px] border",
          checked ? "bg-[#155dfc] border-[#155dfc]" : "bg-white border-[#cbd5e1]",
          "flex items-center justify-center",
          "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/30"
        )}
      >
        {checked ? <Check className="h-3 w-3 text-white" aria-hidden="true" /> : null}
      </button>

      <label
        htmlFor={id}
        className="text-[16px] leading-6 font-medium text-[#4a5565] tracking-[-0.3125px] select-none cursor-pointer"
        onClick={() => onCheckedChange(!checked)}
        aria-label={intl.formatMessage({ id: "checkboxField.ariaLabel" })}
      >
        {label}
      </label>
    </div>
  );
}