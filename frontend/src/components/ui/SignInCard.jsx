import React, { useId, useMemo } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import LabeledInput from "./LabeledInput";
import { cx } from "../utils/cx";

export default function SignInCard({
  values,
  onValuesChange = () => {},
  onSubmit = () => {},
  onForgotPassword = () => {},
  onRememberChange = () => {},
  loading = false,
  useRemoteHeaderIcon = false,
  imgIcon1,
}) {
  const intl = useIntl();
  const usernameId = useId();
  const passwordId = useId();

  const canSubmit = useMemo(() => {
    return Boolean(values.usernameOrEmail?.trim()) && Boolean(values.password);
  }, [values.usernameOrEmail, values.password]);

  return (
    <section
      aria-label={intl.formatMessage({ id: "signInCard.ariaLabel" })}
      className="w-full rounded-2xl border border-[#E5E7EB] bg-white p-6 shadow-[0px_20px_25px_0px_rgba(0,0,0,0.10),0px_8px_10px_0px_rgba(0,0,0,0.10)]"
    >
      <header className="mb-4 flex flex-col gap-2">
        <div className="flex items-center gap-2">
          {useRemoteHeaderIcon ? (
            <img src={imgIcon1} alt="" className="block h-5 w-5" />
          ) : (
            <User size={20} color="#0A0A0A" aria-hidden="true" />
          )}
          <h2 className="m-0 text-base font-medium leading-4 text-[#0A0A0A]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>
        <p className="m-0 text-base leading-6 text-[#717182]">
          {intl.formatMessage({ id: "signInCard.subtitle" })}
        </p>
      </header>

      <form
        className="flex flex-col gap-4"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({ ...values });
        }}
      >
        <LabeledInput
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameLabel" })}
          type="text"
          value={values.usernameOrEmail}
          placeholder={intl.formatMessage({ id: "signInCard.usernamePlaceholder" })}
          autoComplete="username"
          onChange={(next) => onValuesChange({ ...values, usernameOrEmail: next })}
        />

        <LabeledInput
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={values.password}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          autoComplete="current-password"
          onChange={(next) => onValuesChange({ ...values, password: next })}
        />

        <div className="flex min-h-6 flex-wrap items-center justify-between gap-3">
          <label className="inline-flex select-none items-center gap-2 text-base font-medium leading-6 text-[#4A5565]">
            <input
              type="checkbox"
              checked={Boolean(values.rememberMe)}
              onChange={(e) => {
                const next = e.target.checked;
                onValuesChange({ ...values, rememberMe: next });
                onRememberChange(next);
              }}
              className="h-[13px] w-[13px] rounded-[3px] border border-[#CBD5E1] bg-white accent-[#155DFC]"
              aria-label={intl.formatMessage({ id: "signInCard.rememberMeAriaLabel" })}
            />
            {intl.formatMessage({ id: "signInCard.rememberMeLabel" })}
          </label>

          <a
            href="#"
            className={cx(
              "text-sm font-normal leading-5 text-[#155DFC] no-underline hover:underline",
              loading ? "pointer-events-none opacity-70" : ""
            )}
            onClick={(e) => {
              e.preventDefault();
              onForgotPassword();
            }}
          >
            {intl.formatMessage({ id: "signInCard.forgotPassword" })}
          </a>
        </div>

        <button
          type="submit"
          className={cx(
            "h-11 w-full rounded-lg border border-transparent bg-[#030213] text-sm font-medium leading-5 text-white",
            "hover:bg-[#0B0F1A] focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30",
            loading || !canSubmit ? "cursor-not-allowed opacity-70" : "cursor-pointer"
          )}
          disabled={loading || !canSubmit}
          onClick={() => {}}
        >
          {loading
            ? intl.formatMessage({ id: "common.continuing" })
            : intl.formatMessage({ id: "common.continue" })}
        </button>
      </form>
    </section>
  );
}