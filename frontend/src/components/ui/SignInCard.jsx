import React, { useId, useMemo } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import CheckboxField from "./CheckboxField";
import LabeledInput from "./LabeledInput";
import PrimaryButton from "./PrimaryButton";
import TextLink from "./TextLink";

const imgIcon1 = "https://www.figma.com/api/mcp/asset/f07fc150-57a0-4cb4-b08e-5c5fa9544956";

function noop() {}

export default function SignInCard({
  usernameOrEmail,
  password,
  rememberMe,
  onUsernameOrEmailChange = noop,
  onPasswordChange = noop,
  onRememberMeChange = noop,
  onForgotPassword = noop,
  onSubmit = noop,
  headerIconMode = "lucide",
}) {
  const intl = useIntl();

  const headerIcon = useMemo(() => {
    if (headerIconMode === "image") {
      return <img src={imgIcon1} alt="" className="h-5 w-5" aria-hidden="true" />;
    }
    return <User className="h-5 w-5 text-[#0A0A0A]" aria-hidden="true" />;
  }, [headerIconMode]);

  const usernameId = useId();
  const passwordId = useId();

  return (
    <section
      aria-label={intl.formatMessage({ id: "signInCard.ariaLabel" })}
      className="w-full rounded-[14px] border border-[#E5E7EB] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6">
        <div className="flex items-center gap-[6px]">
          {headerIcon}
          <h2 className="text-[16px] font-medium leading-4 tracking-[-0.3125px] text-[#0A0A0A]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>
        <p className="mt-[6px] text-[16px] font-normal leading-6 tracking-[-0.3125px] text-[#717182]">
          {intl.formatMessage({ id: "signInCard.subtitle" })}
        </p>
      </div>

      <form
        className="flex w-full flex-col gap-4 px-6 pb-6 pt-6"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({
            usernameOrEmail,
            password,
            rememberMe,
          });
        }}
      >
        <LabeledInput
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameOrEmailLabel" })}
          type="text"
          value={usernameOrEmail}
          placeholder={intl.formatMessage({ id: "signInCard.usernameOrEmailPlaceholder" })}
          autoComplete="username"
          onChange={onUsernameOrEmailChange}
        />

        <LabeledInput
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={password}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          autoComplete="current-password"
          onChange={onPasswordChange}
        />

        <div className="flex w-full items-center justify-between">
          <CheckboxField
            checked={rememberMe}
            label={intl.formatMessage({ id: "signInCard.rememberMe" })}
            onChange={onRememberMeChange}
          />
          <TextLink
            label={intl.formatMessage({ id: "signInCard.forgotPassword" })}
            onClick={onForgotPassword}
          />
        </div>

        <PrimaryButton label={intl.formatMessage({ id: "signInCard.continue" })} />
      </form>
    </section>
  );
}