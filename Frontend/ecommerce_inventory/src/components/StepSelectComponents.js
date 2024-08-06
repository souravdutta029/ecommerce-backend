import { Autocomplete, Box, FormControl, InputLabel, MenuItem, Select, TextField } from '@mui/material';
import { useEffect } from 'react';
import { useFormContext } from 'react-hook-form';

const StepSelectComponents = ({formConfig, fieldType}) => {
    const {register, formState: {errors}, setValue, watch} = useFormContext();
    const selectFields = formConfig.data.select

    useEffect(() => {
        selectFields.forEach(field => {
            setValue(field.name, field.default || "");
        })
    }, [selectFields, setValue])

    return (
        <Box>
            {selectFields.map((field, index) => (
                <FormControl fullWidth margin='normal' key={field.name}>
                    {/* <InputLabel>{field.label}</InputLabel>
                    <Select 
                    {...register(field.name, {required:field.required})}
                    defaultValue={field.default}
                    error={!!errors[field.name]}
                    label={field.label}>
                        {field.options.map((option, index) => (
                            <MenuItem key={option.id} value={option.id}>{option.value}</MenuItem>
                        ))}
                    </Select> */}
                    <Autocomplete 
                    {...register(field.name, {required:field.required})}
                    options={field.options}
                    getOptionLabel={(option) => option.value}
                    defaultValue={field.options.find(option => option.id === watch(field.name)) || null}
                    onChange={(event, newValue) => {
                        setValue(field.name, newValue?newValue.id : "");
                    }}
                    renderInput={(params) => (
                    <TextField {...params} 
                    label={field.label}
                    variant="outlined"
                    error = {!!errors[field.name]}
                    helperText = {!!errors[field.name] && 'This field is required'} />)}
                    />
                </FormControl>
            ))}
        </Box>
    )
}

export default StepSelectComponents